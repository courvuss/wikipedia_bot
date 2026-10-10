#<=== Импорт ===>
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

#<=== Функция для добавления и регистрации кнопок для бота ===>
def menu_buttons():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn = KeyboardButton(text='Википедия ')
    markup.add(btn)
    return markup










