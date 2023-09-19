from aiogram.types import Message
from aiogram import F
from config import dp, bot
from customLogging import info_


@dp.message(F.text == '/start')
async def command_start(message: Message) -> None:
    """Main handler"""
    await message.delete()
    await message.answer(text='Добро пожаловать') # send message

@dp.message(F.text == '/myid')
async def command_myid(message: Message) -> None:
    """Additional handler"""
    user_id: int = message.from_user.id # type: ignore
    await message.delete()
    await message.answer(text=f'Your user id - {user_id}') # send message

@dp.message()
async def unknown_commands(message: Message) -> None:
    """Unknown commands"""
    await message.delete()


def loadFile() -> None:
    """loading an handler: \"Main\""""
    info_(text='the handler was loaded successfully')