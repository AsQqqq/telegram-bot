"""import"""
import json
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
import asyncio
from aiogram import types, Dispatcher
from create_bot import dp
import time
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import config
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboard import main_kb, other_kb, ktg_news, admins_main_kb, admins_other_kb, panel_kb, nots_kb, news_on_off
from aiogram.dispatcher.filters import Text
import sqlite3
import aiogram
from create_bot import bot

from base.data_base import database_class_push

ID = config.ADMINS

dbp = database_class_push('database.db')

async def admin_panel(message: types.Message):
	if message.from_user.id == ID:
		await message.answer('🖤 Здравствуйте Данила! Вы попали в панель управления!', reply_markup=panel_kb)
	else:
		await message.answer('❌ Вы не можете это использовать')


#рассылка
async def push_all_send(message: types.Message):
	if message.chat.type == 'private':
		if message.from_user.id == ID:
			text = message.text[9:]
			users = dbp.search_status()
			print(users)
			for row in users:				
				try:
					await bot.send_message(row[0], text=text)
				except:
					print('no1')
					dbp.set_active(row[0], 0)
			print('\nуспешно!\n')
		else:
			print('no')



class push(StatesGroup):
	name = State()
	description = State()
	img = State()
	sub = State()


async def add_push(message: types.Message):
  if message.from_user.id == ID:
    await push.name.set()
    await message.reply('💻 Напиши название рассылки', reply_markup=nots_kb)
  else:
    await message.answer('❌ Вы не можете это использовать')
#ловим название
async def name_push(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['name'] = message.text
  await push.next()
  await message.answer('💻 Напишите текст рассылки')
#ловим описание
async def description_push(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['description'] = message.text
  await push.next()
  await message.answer('💻 Загрузите фото')
#ловим фото
async def photo_push(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['img'] = message.photo[0].file_id
  await push.next()
  #надпись с добовлением названия
  await message.answer('💻 Подпишитесь')
#ловим подпись
async def ends_push(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['sub'] = message.text
	await dbp.sql_add_command_ph(state)
	await message.answer('☑️ рассылка отправлена', reply_markup=panel_kb)
	time.sleep(0.2)
	await all_bots_1(message)
	await state.finish()




async def all_bots_1(message: types.Message):
	if message.chat.type == 'private':
		read = await dbp.sql_read_push()
		users = dbp.search_status()
		for ret in read:
			for row in users:
				try:
					await bot.send_photo(row[0], ret[3], f'Оглавление: {ret[1]}\n\nСведения:\n{ret[2]}\n\nСоздатель:  {ret[-1]}')
				except:
					pass
		await dbp.sql_delete_push()




















async def news_conntrol(message: types.Message):
	await message.answer('🌄 Включите или выключите новости', reply_markup=news_on_off)







#остановка новости
async def nots_state(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		current_state = await state.get_state()
		if current_state is None:
			return
		await state.finish()
		await message.answer('❌ дейстивие отменено', reply_markup=panel_kb)



async def all_bots(message: types.Message):
	if message.from_user.id == ID:
		read = await dbp.sql_read_push()
		for ret in read:
			await bot.send_photo(message.from_user.id, ret[3], f'Оглавление:  {ret[1]}\n\nСведения:\n{ret[2]}\n\nСоздатель: {ret[-1]}')
	else:
		await message.answer('❌ Вы не можете это использовать')


def reg_handler_admin(dp:Dispatcher):
	dp.register_message_handler(nots_state, Text(equals='⛔️ Отменить', ignore_case=True), state='*')
	dp.register_message_handler(admin_panel, text='🖲 Панель управления')
	dp.register_message_handler(all_bots, text='🗾 Все новости бота')
	dp.register_message_handler(news_conntrol, text='🌄 Новости')

	dp.register_message_handler(add_push, text='📲 Рассылка', state=None)
	dp.register_message_handler(photo_push, content_types=['photo'], state=push.img)
	dp.register_message_handler(name_push, state=push.name)
	dp.register_message_handler(description_push, state=push.description)
	dp.register_message_handler(ends_push, state=push.sub)
	dp.register_message_handler(push_all_send, commands='sendall')
	