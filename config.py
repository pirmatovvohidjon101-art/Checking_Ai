import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "").strip()
DB_PATH = os.getenv("DB_PATH", "bot_stats.db").strip()
PORT = int(os.getenv("PORT", "10000"))

_raw_admins = os.getenv("ADMIN_IDS", "")
ADMIN_IDS: set[int] = {
    int(item.strip())
    for item in _raw_admins.split(",")
    if item.strip().isdigit()
}
