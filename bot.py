# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from asyncio import sleep

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
from loguru import logger

load_dotenv()
bot = Bot(token=os.environ['TOKEN'])
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'], )
async def send_welcome(message: types.Message):
    await message.answer('Start',
                         reply_markup=ReplyKeyboardMarkup(
                             keyboard=[
                                 [KeyboardButton('Start')]
                             ],
                             resize_keyboard=True
                         ))


@dp.message_handler(lambda message: message.text == 'Start')
async def send_welcome(message: types.Message):
    with open(os.environ['STATUS_FILE'], 'w+') as file_:
        file_.write('1')

    logger.info('Begin start')
    await message.answer('Begin start')

    await sleep(int(os.environ['PAUSE']))

    with open(os.environ['STATUS_FILE'], 'w+') as file_:
        file_.write('0\n')

    logger.info('End start')
    await message.answer('End start')


if __name__ == '__main__':
    logger.info('Pc Power Button bot started')
    executor.start_polling(dp)
