# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from asyncio import sleep

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from loguru import logger

load_dotenv()
bot = Bot(token=os.environ['TOKEN'])
dp = Dispatcher(bot)


@dp.message_handler(commands=['on'])
async def send_welcome(message: types.Message):
    await message.answer('Set status on')

    await sleep(30)

    await message.answer('Set status off')


if __name__ == '__main__':
    logger.info('Pc Power Button bot started')
    executor.start_polling(dp)
