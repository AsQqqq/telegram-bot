import asyncio
from config import bot, dp
from handler import loadMainHandler
from customLogging import info_, warning_

async def startUp() -> None:
    """Launching the bot"""
    info_(text='Bot preparation')
    loadMainHandler()
    warning_(text='The bot is running!')
    await dp.start_polling(bot) # Start bot

if __name__ == "__main__":
    info_(text='Running the code')
    asyncio.run(startUp())