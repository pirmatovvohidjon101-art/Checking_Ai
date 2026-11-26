TEXTS = {
    "uz": {
        "choose_lang": "Tilni tanlang / Выберите язык:",
        "lang_saved": "Til o‘zgartirildi: 🇺🇿 O‘zbekcha",
        "welcome": (
            "👋 Assalomu alaykum!\n\n"
            "Men AI orqali yaratilgan yoki tahrirlangan <b>rasm</b>, <b>ovoz</b> va <b>videolarni</b> "
            "ehtimollik darajasida tahlil qiluvchi botman.\n\n"
            "📎 Menga rasm (yoki fayl), ovozli xabar/audio yoki qisqa video yuboring.\n"
            "⚠️ <i>Eslatma: Hech bir detektor 100% kafolat bermaydi; natija ehtimoliy baho hisoblanadi.</i>"
        ),
        "btn_lang": "🌐 Tilni o‘zgartirish",
        "btn_help": "ℹ️ Qo‘llanma",
        "btn_stats": "📊 Admin statistika",
        "help": (
            "<b>Qanday foydalaniladi?</b>\n"
            "1. <b>Rasm</b> (JPG/PNG) yoki sifatli tekshiruv uchun <b>Fayl</b> yuboring.\n"
            "2. <b>Ovozli xabar</b> yoki audiofayl yuboring.\n"
            "3. <b>Video</b> yoki dumaloq videoxabar yuboring.\n\n"
            "Tizim fayl xususiyatlari va model signallariga asoslanib AI ehtimolini hisoblaydi."
        ),
        "analyzing": "⏳ Fayl tahlil qilinmoqda, biroz kuting...",
        "unsupported": "❌ Ushbu fayl turi hozircha qo‘llab-quvvatlanmaydi. Rasm, audio/ovoz yoki video yuboring.",
        "too_large": "❌ Fayl hajmi juda katta (maksimum 20 MB).",
        "error_process": "⚠️ Faylni qayta ishlashda xatolik yuz berdi. Keyinroq qayta urinib ko‘ring.",
        "not_admin": "⛔ Bu bo‘lim faqat adminlar uchun.",
        "report": (
            "🔎 <b>Tahlil natijasi</b>\n\n"
            "• Tur: <b>{media_type}</b>\n"
            "• AI ehtimoli: <b>{ai_prob}%</b>\n"
            "• Xulosa: <b>{verdict}</b>\n"
            "• Izoh: {details}"
        ),
        "media_photo": "Rasm",
        "media_audio": "Ovoz / Audio",
        "media_video": "Video",
        "verdict_high": "AI bo‘lish ehtimoli yuqori",
        "verdict_mid": "Shubhali / Aralash belgilar",
        "verdict_low": "Tabiiy / AI izlari kam",
        "stats_title": (
            "📊 <b>Bot statistikasi</b>\n\n"
            "👥 Jami foydalanuvchilar: <b>{total_users}</b>\n"
            "🆕 Bugungi yangi foydalanuvchilar: <b>{new_today}</b>\n"
            "🟢 Oxirgi 24 soatda faol: <b>{active_24h}</b>\n"
            "📁 Jami tekshiruvlar: <b>{total_checks}</b>\n"
            "📅 Bugungi tekshiruvlar: <b>{checks_today}</b>\n\n"
            "<b>Turlar bo‘yicha tekshiruvlar:</b>\n"
            "• Rasmlar: <b>{photo_cnt}</b>\n"
            "• Ovozlar: <b>{audio_cnt}</b>\n"
            "• Videolar: <b>{video_cnt}</b>\n\n"
            "<b>Tillar bo‘yicha foydalanuvchilar:</b>\n"
            "• O‘zbek (uz): <b>{uz_cnt}</b>\n"
            "• Rus (ru): <b>{ru_cnt}</b>"
        ),
    },
    "ru": {
        "choose_lang": "Tilni tanlang / Выберите язык:",
        "lang_saved": "Язык изменён: 🇷🇺 Русский",
        "welcome": (
            "👋 Здравствуйте!\n\n"
            "Я бот для вероятностной оценки <b>изображений</b>, <b>голоса</b> и <b>видео</b> "
            "на предмет AI-генерации или монтажа.\n\n"
            "📎 Отправьте фото (или файл), голосовое/аудио или короткое видео.\n"
            "⚠️ <i>Примечание: ни один детектор не даёт 100% гарантии; результат является вероятностной оценкой.</i>"
        ),
        "btn_lang": "🌐 Сменить язык",
        "btn_help": "ℹ️ Инструкция",
        "btn_stats": "📊 Статистика админа",
        "help": (
            "<b>Как пользоваться:</b>\n"
            "1. Отправьте <b>фото</b> или <b>файл</b> (для сохранения метаданных и качества).\n"
            "2. Отправьте <b>голосовое сообщение</b> или аудиофайл.\n"
            "3. Отправьте <b>видео</b> или видеокружок.\n\n"
            "Система оценивает вероятность AI-происхождения по параметрам файла и сигналам анализа."
        ),
        "analyzing": "⏳ Анализирую файл, подождите...",
        "unsupported": "❌ Этот тип файла пока не поддерживается. Отправьте фото, аудио/голосовое или видео.",
        "too_large": "❌ Файл слишком большой (максимум 20 МБ).",
        "error_process": "⚠️ Ошибка при обработке файла. Попробуйте позже.",
        "not_admin": "⛔ Этот раздел доступен только администраторам.",
        "report": (
            "🔎 <b>Результат анализа</b>\n\n"
            "• Тип: <b>{media_type}</b>\n"
            "• Вероятность AI: <b>{ai_prob}%</b>\n"
            "• Вывод: <b>{verdict}</b>\n"
            "• Комментарий: {details}"
        ),
        "media_photo": "Изображение",
        "media_audio": "Голос / Аудио",
        "media_video": "Видео",
        "verdict_high": "Высокая вероятность AI",
        "verdict_mid": "Сомнительно / Смешанные признаки",
        "verdict_low": "Естественно / Мало признаков AI",
        "stats_title": (
            "📊 <b>Статистика бота</b>\n\n"
            "👥 Всего пользователей: <b>{total_users}</b>\n"
            "🆕 Новых сегодня: <b>{new_today}</b>\n"
            "🟢 Активных за 24 часа: <b>{active_24h}</b>\n"
            "📁 Всего проверок: <b>{total_checks}</b>\n"
            "📅 Проверок сегодня: <b>{checks_today}</b>\n\n"
            "<b>По типам медиа:</b>\n"
            "• Изображения: <b>{photo_cnt}</b>\n"
            "• Аудио/голос: <b>{audio_cnt}</b>\n"
            "• Видео: <b>{video_cnt}</b>\n\n"
            "<b>По языкам пользователей:</b>\n"
            "• Узбекский (uz): <b>{uz_cnt}</b>\n"
            "• Русский (ru): <b>{ru_cnt}</b>"
        ),
    },
}


def get_text(lang: str, key: str) -> str:
    lang_dict = TEXTS.get(lang if lang in TEXTS else "uz", TEXTS["uz"])
    return lang_dict.get(key, TEXTS["uz"].get(key, key))
