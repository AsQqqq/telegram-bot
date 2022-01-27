"""import"""
from aiogram import types, Dispatcher
import config
import sqlite3
import time
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text
from create_bot import bot, dp
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import logging
import asyncio
from datetime import datetime
from keyboard import main_kb, other_kb, ktg_news, admins_main_kb, admins_other_kb, panel_kb, bot_kb, game_sub, world_sub, pol_sub, film_sub
from base.data_base import database_class_push, database_class_game, database_class_world, database_class_politika, database_class_film, database_class_bots


ID = config.ADMINS

dbp = database_class_push('database.db')
dcg = database_class_game('database.db')
dcw = database_class_world('database.db')
dcp = database_class_politika('database.db')
dcf = database_class_film('database.db')
dcb = database_class_bots('database.db')

async def start_command(message: types.Message):
	if not dbp.user_exists(message.from_user.id):
		dbp.add_users(message.from_user.id)

	if message.from_user.id == ID:
		await message.answer("🥰 Здравствуйте Данила!\nЯ полностю готов к работе!\n🙂 Жду ваших задач", reply_markup=admins_main_kb)
	else:
		await message.answer('Привет! ☺️\n😉 Выбирай что тебе хочется)', reply_markup=main_kb)


async def ktg(message: types.Message):
	if message.chat.type == 'private':
		if not dbp.user_exists(message.from_user.id):
			dbp.add_users(message.from_user.id)
		await message.answer('подпишись на категорию по душе!', reply_markup=ktg_news)










"""subs game"""

async def game_news(message: types.Message):
	if message.chat.type == 'private':
		if not dcg.user_exists(message.from_user.id):
			dcg.add_users(message.from_user.id)
		await message.answer('❤️ подпишись! будешь всегда первый в новостях', reply_markup=game_sub)

async def games_sub(message: types.Message):
	if not dcg.user_exists(message.from_user.id):
		dcg.add_users(message.from_user.id)
	else:
		dcg.set_active(message.from_user.id, True)
	await message.answer("Вы успешно подписались на новости игр❤️", reply_markup=ktg_news)

async def games_unsub(message: types.Message):
	if not dcg.user_exists(message.from_user.id):
		dcg.add_users(message.from_user.id)
	else:
		dcg.set_active(message.from_user.id, False)
	await message.answer("Вы отписались от новостей!", reply_markup=ktg_news)

"""subs world"""

async def world_news(message: types.Message):
	if message.chat.type == 'private':
		if not dcw.user_exists(message.from_user.id):
			dcw.add_users(message.from_user.id)
		await message.answer('❤️ подпишись! будешь всегда первый в новостях', reply_markup=world_sub)

async def worlds_sub(message: types.Message):
	if not dcw.user_exists(message.from_user.id):
		dcw.add_users(message.from_user.id)
	else:
		dcw.set_active(message.from_user.id, True)
	await message.answer("Вы успешно подписались на мировые новости❤️", reply_markup=ktg_news)

async def worlds_unsub(message: types.Message):
	if not dcw.user_exists(message.from_user.id):
		dcw.add_users(message.from_user.id)
	else:
		dcw.set_active(message.from_user.id, False)
	await message.answer("Вы отписались от новостей!", reply_markup=ktg_news)

"""subs politika"""

async def pol_news(message: types.Message):
	if message.chat.type == 'private':
		if not dcp.user_exists(message.from_user.id):
			dcp.add_users(message.from_user.id)
		await message.answer('❤️ подпишись! будешь всегда первый в новостях', reply_markup=pol_sub)

async def pols_sub(message: types.Message):
	if not dcp.user_exists(message.from_user.id):
		dcp.add_users(message.from_user.id)
	else:
		dcp.set_active(message.from_user.id, True)
	await message.answer("Вы успешно подписались на новости политики❤️", reply_markup=ktg_news)

async def pols_unsub(message: types.Message):
	if not dcp.user_exists(message.from_user.id):
		dcp.add_users(message.from_user.id)
	else:
		dcp.set_active(message.from_user.id, False)
	await message.answer("Вы отписались от новостей!", reply_markup=ktg_news)

"""subs film"""
async def film_news(message: types.Message):
	if message.chat.type == 'private':
		if not dcf.user_exists(message.from_user.id):
			dcf.add_users(message.from_user.id)
		await message.answer('❤️ подпишись! будешь всегда первый в новостях', reply_markup=film_sub)

async def films_sub(message: types.Message):
	if not dcf.user_exists(message.from_user.id):
		dcf.add_users(message.from_user.id)
	else:
		dcf.set_active(message.from_user.id, True)
	await message.answer("Вы успешно подписались на новости фильмов❤️", reply_markup=ktg_news)

async def films_unsub(message: types.Message):
	if not dcf.user_exists(message.from_user.id):
		dcf.add_users(message.from_user.id)
	else:
		dcf.set_active(message.from_user.id, False)
	await message.answer("Вы отписались от новостей!", reply_markup=ktg_news)

"""subs bots"""
async def bot_news(message: types.Message):
	if message.chat.type == 'private':
		if not dcb.user_exists(message.from_user.id):
			dcb.add_users(message.from_user.id)
		await message.answer('❤️ подпишись! будешь всегда первый в новостях', reply_markup=bot_kb)

async def bots_sub(message: types.Message):
	if not dcb.user_exists(message.from_user.id):
		dcb.add_users(message.from_user.id)
	else:
		dcb.set_active(message.from_user.id, True)
	if message.from_user.id == ID:
		await message.answer("Вы успешно подписались на новости бота❤️", reply_markup=admins_main_kb)
	else:
		await message.answer("Вы успешно подписались на новости бота❤️", reply_markup=main_kb)

async def bots_unsub(message: types.Message):
	if not dcb.user_exists(message.from_user.id):
		dcb.add_users(message.from_user.id)
	else:
		dcb.set_active(message.from_user.id, False)
	if message.from_user.id == ID:
		await message.answer("Вы отписались от новостей!", reply_markup=admins_main_kb)
	else:
		await message.answer("Вы отписались от новостей!", reply_markup=main_kb)









async def listsub(message: types.Message):
	await message.answer('подпишись на премиум новости что бы получать свежие данные со 100 сайтов!')


def reg_handler_client(dp:Dispatcher):
	dp.register_message_handler(start_command, commands=['start'])
	dp.register_message_handler(ktg, text='💿 Категории новостей')
	dp.register_message_handler(listsub, text='💽 Мои подписки')
	#subs game
	dp.register_message_handler(game_news, text='🕹 Игры')
	dp.register_message_handler(games_sub, text='🌁 Подписаться')
	dp.register_message_handler(games_unsub, text='🌉 Отписаться')
	#subs world
	dp.register_message_handler(world_news, text='📺 Мир')
	dp.register_message_handler(worlds_sub, text='🌌 Подписаться')
	dp.register_message_handler(worlds_unsub, text='🌃 Отписаться')
	#subs politika
	dp.register_message_handler(pol_news, text='⚖️ Политика')
	dp.register_message_handler(pols_sub, text='🏙 Подписаться')
	dp.register_message_handler(pols_unsub, text='🌆 Отписаться')
	#subs film
	dp.register_message_handler(film_news, text='🎥 Фильмы')
	dp.register_message_handler(films_sub, text='🎆 Подписаться')
	dp.register_message_handler(films_unsub, text='🎇 Отписаться')
	#subs bots
	dp.register_message_handler(bot_news, text='🦾 Подписка на бота')
	dp.register_message_handler(bots_sub, text='🎑 Подписаться')
	dp.register_message_handler(bots_unsub, text='🎆 Отписаться')