from glob import glob 
from random import choice
from utils import get_smile, play_random_numbers, main_keyboard

def greet_user(update, context):
    print('Вызван /start')
    smile = get_smile()
    update.message.reply_text(
        f'Мур, я эхо-бот и отвечаю тебе такими же сообщениями. Мой разработчик распиздяй и не может выучить питон {smile}.',
        reply_markup=main_keyboard())

def talk_to_me(update, context):
    text = update.message.text
    smile = get_smile()
    print(text)
    update.message.reply_text(f'{text} {smile}')

def guess_number(update, context):
    print(context.args)
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_numbers(user_number)
        except (TypeError, ValueError):
                message = "Введите целое число"
    else:
         message = "Введите /guess (число)"
    update.message.reply_text(message)

def helping(update, context):
    print('Помогаю /help')
    update.message.reply_text('Я умею еще не много, вот мои команды: \n \guess - Мы поиграем с тобой в рандомные числа. \n \morning - Я пожелаю тебе доброго утра! \n \support -  Я поддержку тебя в трудную минуту.\n \kino - Я покажу тебе постер любимого фильма.')

def send_images_morning(update, context):
    morning_photo_list = glob('images/good*.jpg')
    morning_photo_filename = choice(morning_photo_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(morning_photo_filename, 'rb'))

def send_images_support(update, context):
    support_photo_list = glob('images/respect*.jpg')
    support_photo_filename = choice(support_photo_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(support_photo_filename, 'rb'))

def send_images_kino(update, context):
    kino_photo_list = glob('images/film*.jp*g')
    kino_photo_filename = choice(kino_photo_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(kino_photo_filename, 'rb'))

def user_coordinates(update, context):
    coords = update.message.location
    update.message.reply_text(
        f"Ваши координаты {coords}",
        reply_markup=main_keyboard()
    )