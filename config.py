import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from customLogging import info_, clear_

clear_() # Clearing the console

def token() -> str:
    """Token Loading"""
    info_(text='Token Launch')
    load_dotenv()
    return os.getenv("TOKEN") # type: ignore # return token

info_(text='Creating a bot')
bot = Bot(token=token()) # Creating a bot
dp = Dispatcher() # Creating a Dispatcher
