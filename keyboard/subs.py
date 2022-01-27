"""imports"""
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

"""game news"""
sub_game = KeyboardButton('🌁 Подписаться')
unsub_game = KeyboardButton('🌉 Отписаться')
"""world news"""
sub_world = KeyboardButton('🌌 Подписаться')
unsub_world = KeyboardButton('🌃 Отписаться')
"""politika news"""
sub_pol = KeyboardButton('🏙 Подписаться')
unsub_pol = KeyboardButton('🌆 Отписаться')
"""film news"""
sub_film = KeyboardButton('🎆 Подписаться')
unsub_film = KeyboardButton('🎇 Отписаться')

"""other"""
back = KeyboardButton('⬅️ Уйти')

"""размер"""
game_sub = ReplyKeyboardMarkup(resize_keyboard=True)
world_sub = ReplyKeyboardMarkup(resize_keyboard=True)
pol_sub = ReplyKeyboardMarkup(resize_keyboard=True)
film_sub = ReplyKeyboardMarkup(resize_keyboard=True)

"""клавиатура"""
game_sub.add(sub_game).insert(unsub_game).add(back)
world_sub.add(sub_world).insert(unsub_world).add(back)
pol_sub.add(sub_pol).insert(unsub_pol).add(back)
film_sub.add(sub_film).insert(unsub_film).add(back)