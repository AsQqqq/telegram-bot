"""ИМПОРТЫ"""
import config
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
storage=MemoryStorage()
import json
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
import asyncio

"""ПОДКЛЮЧЕНИЕ"""
bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)