from logic import DB_Manager
from config import *
from telebot import TeleBot

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, """Привет! Я бот-менеджер проектов
Помогу тебе сохранить твои проекты и информацию о них!) 
""")

@bot.message_handler(commands=['top'])
def start_command(message):
    bot.send_message(message.chat.id, """Привет! Я бот который поможет тебе выбрать игру!) """)
    genre = message.text.split(" ")[1]
    tops = manager.get_genre(genre)
    for i in tops:
        bot.send_message(message.chat.id, f"{i[1]}, {i[4]}")

@bot.message_handler(commands=['random'])
def start_command(message):
    bot.send_message(message.chat.id, """Привет! Это рандомные три игры!) """)
    bot.send_message(message.chat.id, manager.get_random_game())
if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
    bot.infinity_polling() 