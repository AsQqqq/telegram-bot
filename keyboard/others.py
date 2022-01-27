"""imports"""
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

"""кнопки"""
#ktg
game = KeyboardButton('🕹 Игры')
news = KeyboardButton('📺 Мир')
politika = KeyboardButton('⚖️ Политика')
film = KeyboardButton('🎥 Фильмы')

addsite = KeyboardButton('➕ Добавить категорию')

back = KeyboardButton('⬅️ Назад')
nots = KeyboardButton('⛔️ Отменить')

#bot sub
botsub = KeyboardButton('🎑 Подписаться')
botunsub = KeyboardButton('🎆 Отписаться')

"""размер"""
ktg_news = ReplyKeyboardMarkup(resize_keyboard=True)
nots_kb = ReplyKeyboardMarkup(resize_keyboard=True)
bot_kb = ReplyKeyboardMarkup(resize_keyboard=True)

"""клавиатура"""
ktg_news.add(game).insert(news).add(politika).insert(film).add(addsite).insert(back)
bot_kb.add(botsub).insert(botunsub).add(back)
nots_kb.add(nots)