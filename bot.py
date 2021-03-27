import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Мур')

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main ():
    #Создаем бота и передаем ему ключ для авторизации на серверах Telegram 
    mybot = Updater(settings.API_KEY, use_context=True)
    
    #Призвоили переменной диспетчера, чтобы каждый раз не писать код
    dp = mybot.dispatcher
    #Пишем на какую команду и как будет реагировать бот
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот стартовал')

    #Командуем боту ходить в телеграм за сообщениями 
    mybot.start_polling()
    #Запускаем бота, он будет работать пока мы его не остановим принудительно
    mybot.idle()

if __name__== "__main__":
    main()

