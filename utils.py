from emoji import emojize
from random import choice, randint
from telegram import ReplyKeyboardMarkup, KeyboardButton

import settings 

def get_smile():
    smile = choice(settings.USER_EMOJI)
    return emojize(smile, use_aliases=True)

def play_random_numbers(user_number):
    bot_number = randint(user_number -10, user_number +10)
    if user_number > bot_number:
        message = f"Ты загадал {user_number}, я загадал {bot_number}, ты выиграл!"
    elif user_number == bot_number:
        message = f"Ты загадал {user_number}, я загадал {bot_number}, ничья!"
    else:
        message = f"Ты загадал {user_number}, я загадал {bot_number}, я выиграл!"
    return message

def main_keyboard():
    return ReplyKeyboardMarkup([
        ['Доброе утро!' , 'Поддержи меня'],
        ['Посоветуй фильм' , 'Поиграй в числа', KeyboardButton ('Мои координаты', request_location=True)]
    ]
    )