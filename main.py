#Импорты библиотек
from telebot.types import Message, ReplyKeyboardRemove
import dotenv
import telebot
import os
import wikipedia
from reply import menu_buttons

wikipedia.set_lang('ru')
#<=== Загрузка dot-env для загрузки токена если будете запускать свеого бота на основе кода моего создайте файл .env
# и в этом текстовом файле сделайте констранту(с большой буквы) .env обязательно пример-  TOKEN=(И сюда без лишних знаков вставить токен вашего бота)===>
dotenv.load_dotenv()
bot = telebot.TeleBot(os.getenv("TOKEN"))

@bot.message_handler(commands=['start'])
def start(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Вас приветствует бот для статей википидии в телеграмме', reply_markup=menu_buttons())

@bot.message_handler(regexp='Википедия')
def reaction_wikipedia(message: Message):
    chat_id = message.chat.id
    bot.delete_message(chat_id, message.message_id)
    bot.send_message(chat_id, 'Введите текст для поиска в Википедии: ', reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(message, get_text_for_wikipedia)
def get_text_for_wikipedia(message: Message):
    chat_id = message.chat.id
    text = message.text
    try:
        responce = wikipedia.summary(text, sentences=100)
    except:
        responce = 'Вы ввели неккоректный запрос повторите попытку!'
    bot.send_message(chat_id, responce, reply_markup=menu_buttons())


bot.infinity_polling()