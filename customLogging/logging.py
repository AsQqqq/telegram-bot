import logging
from colorama import Fore, Style
from os import system
import datetime

path_to_logs = "log/"
terminal_cleanup_command = 'clear'


def clear_() -> None:
    """Clearing the console"""
    system(terminal_cleanup_command)

def info_(text: str) -> None:
    """Output to the console in style: \"INFO\""""
    logger.info(text)

def warning_(text: str) -> None:
    """Output to the console in style: \"WARNING\""""
    logger.warning(text)

def error_(text: str) -> None:
    """Output to the console in style: \"ERROR\""""
    logger.error(text)


logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(levelname)s : %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.propagate = False # type: ignore
logger.addHandler(console_handler)
logging.addLevelName(logging.INFO, f"[{Fore.GREEN}{logging.getLevelName(logging.INFO)}{Style.RESET_ALL}]")
logging.addLevelName(logging.WARNING, f"[{Fore.YELLOW}{logging.getLevelName(logging.WARNING)}{Style.RESET_ALL}]")
logging.addLevelName(logging.ERROR, f"[{Fore.RED}{logging.getLevelName(logging.ERROR)}{Style.RESET_ALL}]")

now = datetime.datetime.now()
date = now.strftime("%Y%m%d")
time = now.strftime("%H%M")
result_date = result = date + "-" + time

logging.basicConfig(filename=f"{path_to_logs}{result_date}.txt",
    filemode='a',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG)