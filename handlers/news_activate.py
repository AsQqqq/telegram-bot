"""ИМПОРТЫ"""
from aiogram import types, Dispatcher
from create_bot import dp
import json, string
from keyboard import main_kb, other_kb, ktg_news, admins_main_kb, admins_other_kb, panel_kb
import config
from pars.game_pars import check_news_update
import sqlite3
import asyncio
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
import time
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text
from base import data_base
from create_bot import bot

ID = config.ADMINS



#коннект с базой
connect = sqlite3.connect('database.db')
cursor = connect.cursor()

#функция проверки на новости
stop_polling_site = None

async def get_news(message: types.Message):
	fresh_news_game = check_news_update()

	x = cursor.execute('SELECT * FROM sub_game WHERE status=True').fetchall()
	ids = []
	for i in x:
		ids.append(i[1])

	if len(fresh_news_game) >= 1:
		for k, v in sorted(fresh_news_game.items()):
			news_1 = f'{hlink(v["aubl_title"], v["aubl_url_split_print"])}\n{hcode(v["dates_id_print"])}'
			try:
				for i in ids:
					await bot.send_message(chat_id = i, text=news_1)
			except:
				pass
			print('новость опубликована(игры)')
			time.sleep(0.8)
	else:
		pass

#включение новости
async def start_polling_news(message: types.Message):
	if message.from_user.id == ID:
		global stop_polling_site
		if stop_polling_site is not None:
			await message.answer("Мы уже проверяем новости", reply_markup=panel_kb)
			return
		else:
			await message.answer("проверка включена", reply_markup=panel_kb)
		stop_polling_site = asyncio.Event()
		while True:
			try:
				await asyncio.wait_for(stop_polling_site.wait(), timeout=15)
			except asyncio.TimeoutError:
				try:
					await get_news(message)
				except:
					pass
			else:
				break
		stop_polling_site = None
	else:
		await message.answer('❌ Вы не можете это использовать')

#выключение новости
async def stop_polling_news(message: types.Message):
	if message.from_user.id == ID:
		global stop_polling_site
		if stop_polling_site is None:
			await message.answer("Мы и так не проверяем новости", reply_markup=panel_kb)
		else:
			await message.answer('Проверка новостей выключена', reply_markup=panel_kb)
			stop_polling_site.set()
	else:
		await message.answer('❌ Вы не можете это использовать')


"""start"""
def reg_handler_game_news(dp:Dispatcher):
	dp.register_message_handler(start_polling_news, text='✅ Включить')
	dp.register_message_handler(stop_polling_news, text='❌ Выключить')