from aiogram import Bot, Dispatcher
from aiohttp import web
from dotenv import load_dotenv

import sys, os
import asyncio, logging


from app.handlers import router

load_dotenv()

bot = Bot(token=str(os.getenv("BOT_TOKEN")))
dp = Dispatcher()
dp.include_router(router)

async def handle(request):
    return web.Response(text="Bot is alive")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", handle)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", int(os.getenv("PORT", 8080)))
    await site.start()
    print("✅ Bot started and server is running...")

async def main():
    await start_web_server()
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout, format="%(asctime)s %(levelname)s %(message)s")
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.warning("Бот отключен")