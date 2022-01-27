"""ИМПОРТЫ"""
import os
from base import data_base
from aiogram.utils import executor
from create_bot import dp
from base import data_base
from handlers import user, admin, other, news_activate
import time, sys
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from pars.game_pars import check_news_update

user.reg_handler_client(dp)
admin.reg_handler_admin(dp)
news_activate.reg_handler_game_news(dp)
other.reg_handler_other(dp)

"""PRINT START"""
def bot_start():
	print('\nбот запустился!')

"""CLEAR"""
def cmd_clear():
	try:
		os.system('cls')
	except:
		os.system('clear')
	print('dev: AsQ\n')

"""START"""
async def on_startup(_):
	try:
		os.system('cls')
	except:
		os.system('clear')
	data_base.sub_bot()
	data_base.push_cache()
	data_base.sub_game()
	data_base.sub_world()
	data_base.sub_politika()
	data_base.sub_film()
	bot_start()

#запуск бота
if __name__ == "__main__":
  executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
  cmd_clear()