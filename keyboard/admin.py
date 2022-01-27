"""imports"""
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


"""кнопки"""
panel = KeyboardButton('🖲 Панель управления')

news = KeyboardButton('🌄 Новости')
push = KeyboardButton('📲 Рассылка')
all_news_bot = KeyboardButton('🗾 Все новости бота')

ktg = KeyboardButton('💿 Категории новостей')
bsub = KeyboardButton('🦾 Подписка на бота')
premsub = KeyboardButton('💽 Мои подписки')

nexts = KeyboardButton('➡️ Далее')

helper = KeyboardButton('❤️ Помочь проекту')
nastochat = KeyboardButton('⁉️ Пожаловаться')
message_adm = KeyboardButton('💛 Сообщение админу')

back = KeyboardButton('⬅️ Назад')

vkl = KeyboardButton('✅ Включить')
vikl = KeyboardButton('❌ Выключить')

down = KeyboardButton('⬅️ Вернуться')

"""размер"""
admins_main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
admins_other_kb = ReplyKeyboardMarkup(resize_keyboard=True)
panel_kb = ReplyKeyboardMarkup(resize_keyboard=True)
news_on_off = ReplyKeyboardMarkup(resize_keyboard=True)

"""клавиатура"""
panel_kb.add(news).insert(push).add(all_news_bot).insert(back)
admins_main_kb.add(ktg).insert(bsub).add(premsub).insert(nexts).add(panel)
admins_other_kb.add(helper).insert(nastochat).add(message_adm).insert(back).add(panel)
news_on_off.add(vkl).insert(vikl).add(down)