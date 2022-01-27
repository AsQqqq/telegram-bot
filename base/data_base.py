"""import"""
import sqlite3 as sq
import sqlite3
from create_bot import bot
import time
from aiogram import types, Dispatcher
from create_bot import dp

base = sq.connect('database.db')
cur = base.cursor()


def sub_bot():
	base.execute('CREATE TABLE IF NOT EXISTS sub_bot(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id VARCHAR (255) NOT NULL, status BOOLEAN NOT NULL DEFAULT (TRUE))')
	if base:
		print('\nбаза данных 1 подключилась')

def push_cache():
	base.execute('CREATE TABLE IF NOT EXISTS push_cache(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, img TEXT, sub TEXT)')
	if base:
		print('\nбаза данных 2 подключилась')

def sub_game():
	base.execute('CREATE TABLE IF NOT EXISTS sub_game(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id VARCHAR (255) NOT NULL, status BOOLEAN NOT NULL DEFAULT (FALSE))')
	if base:
		print('\n"новости игр" - база данных подключилась')

def sub_world():
	base.execute('CREATE TABLE IF NOT EXISTS sub_world(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id VARCHAR (255) NOT NULL, status BOOLEAN NOT NULL DEFAULT (FALSE))')
	if base:
		print('\n"новости мира" - база данных подключилась')

def sub_politika():
	base.execute('CREATE TABLE IF NOT EXISTS sub_politika(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id VARCHAR (255) NOT NULL, status BOOLEAN NOT NULL DEFAULT (FALSE))')
	if base:
		print('\n"новости политики" - база данных подключилась')

def sub_film():
	base.execute('CREATE TABLE IF NOT EXISTS sub_film(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id VARCHAR (255) NOT NULL, status BOOLEAN NOT NULL DEFAULT (FALSE))')
	if base:
		print('\n"новости фильмов" - база данных подключилась')

#рассылка
class database_class_push:
	def __init__(self, database):
		self.connection = sqlite3.connect(database)
		self.cursor = self.connection.cursor()

	#поиск пользователя
	def user_exists(self, user_id):
		with self.connection:
			result = self.cursor.execute('SELECT * FROM `sub_bot` WHERE `user_id` = ?', (user_id,)).fetchmany(1)
			return bool(len(result))

	#добовление пользователя
	def add_users(self, user_id):
		with self.connection:
			return self.cursor.execute('INSERT INTO `sub_bot` (user_id) VALUES (?)', (user_id,))

	#изменения актива
	def set_active(self, user_id, status):
		with self.connection:
			return self.cursor.execute('UPDATE `sub_bot` SET `status` = ? WHERE `user_id` = ?', (status, user_id,))

	#вывод всех активных пользователей
	def get_users(self):
		with self.connection:
			return self.cursor.execute('SELECT `user_id`, `status` FROM `sub_bot`').fetchall()

	#поиск id с активной подпиской
	def search_status(self):
		with self.connection:
			return self.cursor.execute('SELECT `user_id` FROM `sub_bot` WHERE status = True').fetchall()

	#запись рассылки в базу данных
	async def sql_add_command_ph(self, state):
		with self.connection:
			async with state.proxy() as data:
				self.cursor.execute('INSERT INTO push_cache (name, description, img, sub) VALUES (?, ?, ?, ?)', tuple(data.values()))
				base.commit()

	#чтение рассылки из базы данных
	async def sql_read_push(self):
		with self.connection:
			return self.cursor.execute('SELECT * FROM push_cache').fetchall()

	async def sql_delete_push(self):
		with self.connection:
			return self.cursor.execute('DELETE FROM push_cache')







"""подписка на новости игр"""

class database_class_game:
	def __init__(self, database):
		self.connection = sqlite3.connect(database)
		self.cursor = self.connection.cursor()

	#поиск пользователя
	def user_exists(self, user_id):
		with self.connection:
			result = self.cursor.execute('SELECT * FROM `sub_game` WHERE `user_id` = ?', (user_id,)).fetchmany(1)
			return bool(len(result))

	#добовление пользователя
	def add_users(self, user_id):
		with self.connection:
			return self.cursor.execute('INSERT INTO `sub_game` (user_id) VALUES (?)', (user_id,))

	#изменения актива
	def set_active(self, user_id, status):
		with self.connection:
			return self.cursor.execute('UPDATE `sub_game` SET `status` = ? WHERE `user_id` = ?', (status, user_id,))

	#вывод всех активных пользователей
	def get_users(self):
		with self.connection:
			return self.cursor.execute('SELECT `user_id`, `status` FROM `sub_game`').fetchall()

	#поиск id с активной подпиской
	def search_status(self):
		with self.connection:
			return self.cursor.execute('SELECT `user_id` FROM `sub_game` WHERE status = True').fetchall()



"""подписка на мировые новости"""

class database_class_world:
	def __init__(self, database):
		self.connection = sqlite3.connect(database)
		self.cursor = self.connection.cursor()

	#поиск пользователя
	def user_exists(self, user_id):
		with self.connection:
			result = self.cursor.execute('SELECT * FROM `sub_world` WHERE `user_id` = ?', (user_id,)).fetchmany(1)
			return bool(len(result))

	#добовление пользователя
	def add_users(self, user_id):
		with self.connection:
			return self.cursor.execute('INSERT INTO `sub_world` (user_id) VALUES (?)', (user_id,))
			print('ok')

	#изменения актива
	def set_active(self, user_id, status):
		with self.connection:
			return self.cursor.execute('UPDATE `sub_world` SET `status` = ? WHERE `user_id` = ?', (status, user_id,))

	#вывод всех активных пользователей
	def get_users(self):
		with self.connection:
			return self.cursor.execute('SELECT `user_id`, `status` FROM `sub_world`').fetchall()

	#поиск id с активной подпиской
	def search_status(self):
		with self.connection:
			return self.cursor.execute('SELECT `user_id` FROM `sub_world` WHERE status = True').fetchall()








"""подписка на политические новости"""

class database_class_politika:
	def __init__(self, database):
		self.connection = sqlite3.connect(database)
		self.cursor = self.connection.cursor()

	#поиск пользователя
	def user_exists(self, user_id):
		with self.connection:
			result = self.cursor.execute('SELECT * FROM `sub_politika` WHERE `user_id` = ?', (user_id,)).fetchmany(1)
			return bool(len(result))

	#добовление пользователя
	def add_users(self, user_id):
		with self.connection:
			return self.cursor.execute('INSERT INTO `sub_politika` (user_id) VALUES (?)', (user_id,))
			print('ok')

	#изменения актива
	def set_active(self, user_id, status):
		with self.connection:
			return self.cursor.execute('UPDATE `sub_politika` SET `status` = ? WHERE `user_id` = ?', (status, user_id,))

	#вывод всех активных пользователей
	def get_users(self):
		with self.connection:
			return self.cursor.execute('SELECT `user_id`, `status` FROM `sub_politika`').fetchall()

	#поиск id с активной подпиской
	def search_status(self):
		with self.connection:
			return self.cursor.execute('SELECT `user_id` FROM `sub_politika` WHERE status = True').fetchall()








"""подписка на новости фильмов"""

class database_class_film:
	def __init__(self, database):
		self.connection = sqlite3.connect(database)
		self.cursor = self.connection.cursor()

	#поиск пользователя
	def user_exists(self, user_id):
		with self.connection:
			result = self.cursor.execute('SELECT * FROM `sub_film` WHERE `user_id` = ?', (user_id,)).fetchmany(1)
			return bool(len(result))

	#добовление пользователя
	def add_users(self, user_id):
		with self.connection:
			return self.cursor.execute('INSERT INTO `sub_film` (user_id) VALUES (?)', (user_id,))
			print('ok')

	#изменения актива
	def set_active(self, user_id, status):
		with self.connection:
			return self.cursor.execute('UPDATE `sub_film` SET `status` = ? WHERE `user_id` = ?', (status, user_id,))

	#вывод всех активных пользователей
	def get_users(self):
		with self.connection:
			return self.cursor.execute('SELECT `user_id`, `status` FROM `sub_film`').fetchall()

	#поиск id с активной подпиской
	def search_status(self):
		with self.connection:
			return self.cursor.execute('SELECT `user_id` FROM `sub_film` WHERE status = True').fetchall()

"""подписка на новости фильмов"""

class database_class_bots:
	def __init__(self, database):
		self.connection = sqlite3.connect(database)
		self.cursor = self.connection.cursor()

	#поиск пользователя
	def user_exists(self, user_id):
		with self.connection:
			result = self.cursor.execute('SELECT * FROM `sub_bot` WHERE `user_id` = ?', (user_id,)).fetchmany(1)
			return bool(len(result))

	#добовление пользователя
	def add_users(self, user_id):
		with self.connection:
			return self.cursor.execute('INSERT INTO `sub_bot` (user_id) VALUES (?)', (user_id,))
			print('ok')

	#изменения актива
	def set_active(self, user_id, status):
		with self.connection:
			return self.cursor.execute('UPDATE `sub_bot` SET `status` = ? WHERE `user_id` = ?', (status, user_id,))

	#вывод всех активных пользователей
	def get_users(self):
		with self.connection:
			return self.cursor.execute('SELECT `user_id`, `status` FROM `sub_bot`').fetchall()

	#поиск id с активной подпиской
	def search_status(self):
		with self.connection:
			return self.cursor.execute('SELECT `user_id` FROM `sub_bot` WHERE status = True').fetchall()

