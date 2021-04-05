import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from handlers import (greet_user, talk_to_me, guess_number, helping, send_images_morning,
                        send_images_support, send_images_kino, user_coordinates)

import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)


def main ():
    #Создаем бота и передаем ему ключ для авторизации на серверах Telegram 
    mybot = Updater(settings.API_KEY, use_context=True)
    
    #Приcвоили переменной диспетчера, чтобы каждый раз не писать код
    dp = mybot.dispatcher
    #Пишем на какую команду и как будет реагировать бот
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('help', helping))
    dp.add_handler(CommandHandler('guess', guess_number))
    dp.add_handler(CommandHandler('morning', send_images_morning))
    dp.add_handler(CommandHandler('support', send_images_support))
    dp.add_handler(CommandHandler('kino', send_images_kino))
    dp.add_handler(MessageHandler(Filters.regex('^(Доброе утро!)$'), send_images_morning))
    dp.add_handler(MessageHandler(Filters.regex('^(Посоветуй фильм)$'), send_images_kino))
    dp.add_handler(MessageHandler(Filters.regex('^(Поиграй в числа)$'), guess_number))
    dp.add_handler(MessageHandler(Filters.regex('^(Поддержи меня)$'), send_images_support))
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот стартовал')

    #Командуем боту ходить в телеграм за сообщениями 
    mybot.start_polling()
    #Запускаем бота, он будет работать пока мы его не остановим принудительно
    mybot.idle()

if __name__== "__main__":
    main()

