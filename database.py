import sqlite3
from datetime import datetime, timedelta, timezone
import psycopg
from psycopg.rows import dict_row


class Database:
    def __init__(self, database_url: str = "", db_path: str = "bot_stats.db"):
        self.use_postgres = bool(database_url)
        if self.use_postgres:
            self.conn = psycopg.connect(database_url, row_factory=dict_row, autocommit=True)
        else:
            self.conn = sqlite3.connect(db_path, check_same_thread=False)
            self.conn.row_factory = sqlite3.Row
        self._create_tables()

    def _ph(self, query: str) -> str:
        return query.replace("?", "%s") if self.use_postgres else query

    def _execute(self, query: str, params: tuple = ()):
        sql = self._ph(query)
        if self.use_postgres:
            with self.conn.cursor() as cur:
                cur.execute(sql, params)
                if cur.description:
                    return cur.fetchall()
                return []
        else:
            with self.conn:
                cur = self.conn.execute(sql, params)
                if cur.description:
                    return cur.fetchall()
                return []

    def _create_tables(self) -> None:
        pk_auto = "SERIAL PRIMARY KEY" if self.use_postgres else "INTEGER PRIMARY KEY AUTOINCREMENT"
        self._execute(
            f"""
            CREATE TABLE IF NOT EXISTS users (
                user_id BIGINT PRIMARY KEY,
                username TEXT,
                full_name TEXT,
                lang TEXT DEFAULT 'uz',
                created_at TEXT NOT NULL,
                last_active TEXT NOT NULL
            )
            """
        )
        self._execute(
            f"""
            CREATE TABLE IF NOT EXISTS checks (
                id {pk_auto},
                user_id BIGINT NOT NULL,
                media_type TEXT NOT NULL,
                ai_prob INTEGER NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )

    @staticmethod
    def _now_iso() -> str:
        return datetime.now(timezone.utc).isoformat()

    def upsert_user(self, user_id: int, username: str | None, full_name: str | None) -> str:
        now = self._now_iso()
        rows = self._execute("SELECT lang FROM users WHERE user_id = ?", (user_id,))
        if not rows:
            self._execute(
                """
                INSERT INTO users (user_id, username, full_name, lang, created_at, last_active)
                VALUES (?, ?, ?, 'uz', ?, ?)
                """,
                (user_id, username, full_name, now, now),
            )
            return "uz"

        self._execute(
            """
            UPDATE users
            SET username = ?, full_name = ?, last_active = ?
            WHERE user_id = ?
            """,
            (username, full_name, now, user_id),
        )
        lang = rows[0]["lang"]
        return lang if lang in ("uz", "ru") else "uz"

    def set_lang(self, user_id: int, lang: str) -> None:
        if lang not in ("uz", "ru"):
            return
        now = self._now_iso()
        self._execute(
            "UPDATE users SET lang = ?, last_active = ? WHERE user_id = ?",
            (lang, now, user_id),
        )

    def get_lang(self, user_id: int) -> str:
        rows = self._execute("SELECT lang FROM users WHERE user_id = ?", (user_id,))
        if rows and rows[0]["lang"] in ("uz", "ru"):
            return rows[0]["lang"]
        return "uz"

    def log_check(self, user_id: int, media_type: str, ai_prob: int) -> None:
        now = self._now_iso()
        self._execute(
            """
            INSERT INTO checks (user_id, media_type, ai_prob, created_at)
            VALUES (?, ?, ?, ?)
            """,
            (user_id, media_type, ai_prob, now),
        )
        self._execute(
            "UPDATE users SET last_active = ? WHERE user_id = ?",
            (now, user_id),
        )

    def get_stats(self) -> dict:
        now_dt = datetime.now(timezone.utc)
        today_start = now_dt.replace(hour=0, minute=0, second=0, microsecond=0).isoformat()
        last_24h = (now_dt - timedelta(hours=24)).isoformat()

        total_users = self._execute("SELECT COUNT(*) AS c FROM users")[0]["c"]
        new_today = self._execute(
            "SELECT COUNT(*) AS c FROM users WHERE created_at >= ?", (today_start,)
        )[0]["c"]
        active_24h = self._execute(
            "SELECT COUNT(*) AS c FROM users WHERE last_active >= ?", (last_24h,)
        )[0]["c"]

        total_checks = self._execute("SELECT COUNT(*) AS c FROM checks")[0]["c"]
        checks_today = self._execute(
            "SELECT COUNT(*) AS c FROM checks WHERE created_at >= ?", (today_start,)
        )[0]["c"]

        def count_media(m_type: str) -> int:
            return self._execute(
                "SELECT COUNT(*) AS c FROM checks WHERE media_type = ?", (m_type,)
            )[0]["c"]

        def count_lang(lang_code: str) -> int:
            return self._execute(
                "SELECT COUNT(*) AS c FROM users WHERE lang = ?", (lang_code,)
            )[0]["c"]

        return {
            "total_users": total_users,
            "new_today": new_today,
            "active_24h": active_24h,
            "total_checks": total_checks,
            "checks_today": checks_today,
            "photo_cnt": count_media("photo"),
            "audio_cnt": count_media("audio"),
            "video_cnt": count_media("video"),
            "uz_cnt": count_lang("uz"),
            "ru_cnt": count_lang("ru"),
        }
