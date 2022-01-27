"""ИМПОРТЫ"""
from aiogram import types, Dispatcher
from create_bot import dp
import json, string
from keyboard import main_kb, other_kb, ktg_news, admins_main_kb, admins_other_kb, panel_kb
import config

ID = config.ADMINS

"""неизвестное сообщение"""
async def no_message(message: types.Message):
  if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
    .intersection(set(json.load(open('other/no_message.json')))) != set():
    await message.reply('маты запрещены.')
    await message.delete()
  else:
    await message.answer('я не знаю такие слова... напиши /start')

async def others(message: types.Message):
	if message.from_user.id == ID:
		await message.answer('⬅️ Назад', reply_markup=admins_main_kb)
	else:
		await message.answer('⬅️ Назад', reply_markup=main_kb)

async def nexts(message: types.Message):
	if message.from_user.id == ID:
		await message.answer('➡️ Далее', reply_markup=admins_other_kb)
	else:
		await message.answer('➡️ Далее', reply_markup=other_kb)


async def backs(message: types.Message):
	if message.from_user.id == ID:
		await message.answer('➡️ Далее', reply_markup=panel_kb)
	else:
		await message.answer('❌ Вы не можете это использовать')

async def back_news(message: types.Message):
	await message.answer('➡️ Далее', reply_markup=ktg_news)

"""start"""
def reg_handler_other(dp:Dispatcher):
	dp.register_message_handler(nexts, text='➡️ Далее')
	dp.register_message_handler(others, text='⬅️ Назад')
	dp.register_message_handler(backs, text='⬅️ Вернуться')
	dp.register_message_handler(back_news, text='⬅️ Уйти')
	dp.register_message_handler(no_message)