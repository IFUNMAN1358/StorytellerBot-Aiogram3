from os import getenv

from aiogram import Dispatcher, Bot
from asyncio import run

from dotenv import load_dotenv

from handlers.start_handler import router as start_router
from callbacks.chapter_1_callback import router as chapter_1_callback
from callbacks.chapter_2_callback import router as chapter_2_callback
from callbacks.chapter_3_callback import router as chapter_3_callback


load_dotenv()


async def start():
    bot = Bot(token=getenv('TOKEN_BOT'))
    dp = Dispatcher()

    dp.include_routers(start_router,
                       chapter_1_callback,
                       chapter_2_callback,
                       chapter_3_callback)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    run(start())