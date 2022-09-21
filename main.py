"""by WHITE DUKE"""
import telebot

from Parser import *

from log import *

bot = telebot.Telebot(TelegramToken)
bot.worker_pool = telebot.util.ThreadPool(num_threads=5)


@bot.message_handler(commands=['Help', 'help', 'start'])
def help(command):
    bot.send_message(command.chat.id,
                     'ᅠᅠᅠᅠ ⚙️ *Commands* ⚙️'
                     '\n'
                     '\n'
                     '\n*/scraping* - _🎦scraping movies with ivi 🎦_',
                     parse_mode='Markdown')


@bot.message_handler(commands='scraping')
def bot_message(command):
    bot.send_message(command.chat.id, '=============TOP============')
    parser_film = Film()
    Film.parse_film(parser_film)
    film_top = ''.join(parser_film.rating_and_film)
    bot.send_message(command.chat.id, film_top)


if __name__ == "__main__":
    bot.polling(non_stop=True)