from aiohttp import web
from config import ADMIN_IDS, BOT_TOKEN, DATABASE_URL, DB_PATH, PORT

db = Database(database_url=DATABASE_URL, db_path=DB_PATH)


async def start_health_server() -> web.AppRunner:
    async def health_handler(_request: web.Request) -> web.Response:
        return web.Response(text="OK")

    app = web.Application()
    app.router.add_get("/", health_handler)
    app.router.add_get("/health", health_handler)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host="0.0.0.0", port=PORT)
    await site.start()
    return runner


async def main() -> None:
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN topilmadi. Environment Variables ni tekshiring.")

    runner = await start_health_server()
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()
    dp.include_router(router)

    try:
        await dp.start_polling(bot)
    finally:
        await runner.cleanup()
        await bot.session.close()
