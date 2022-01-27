"""imports"""
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

"""кнопки"""
ktg = KeyboardButton('💿 Категории новостей')
bsub = KeyboardButton('🦾 Подписка на бота')
premsub = KeyboardButton('💽 Мои подписки')

nexts = KeyboardButton('➡️ Далее')

helper = KeyboardButton('❤️ Помочь проекту')
nastochat = KeyboardButton('⁉️ Пожаловаться')
message_adm = KeyboardButton('💛 Сообщение админу')
back = KeyboardButton('⬅️ Назад')



"""размер"""
main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
other_kb = ReplyKeyboardMarkup(resize_keyboard=True)

"""клавиатура"""
main_kb.add(ktg).insert(bsub).add(premsub).insert(nexts)
other_kb.add(helper).insert(nastochat).add(message_adm).insert(back)