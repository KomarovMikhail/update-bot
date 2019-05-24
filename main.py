# -*- coding: utf-8 -*-
from config import *
import telebot
from flask import Flask, request
import logging
from subscribes import *
from spreadsheet import *
from stats import *
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta


bot = telebot.TeleBot(TOKEN)

# scheduler = BackgroundScheduler()
# scheduler.start()

# init database
create_subscribes()
create_stats()


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    text = 'Дароу! Если ты подпишешься на мои обновления, я буду оповещать тебя, как только состояние базы изменится. ' \
           'Список доступных команд:\n/help - список доступных команд\n' \
           '/get - получить полную статистику на данный момент\n/out - отписаться от рассылки\n' \
           '/in - подписаться на рассылку'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['get'])
def handle_get(message):
    stats = select_all_stats()
    text = 'Текущая статистика:\n'
    for item in stats:
        text += item
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['in'])
def handle_in(message):
    add_to_subscribes(message.chat.id)
    bot.send_message(message.chat.id, "Готово! Я подписал тебя на рассылку.")


@bot.message_handler(commands=['out'])
def handle_out(message):
    remove_from_subscribes(message.chat.id)
    bot.send_message(message.chat.id, "Обидно, конечно, ну ладно. Атписка оформлена.")


@bot.message_handler(content_types=["text"])
def unknown_messages(message):
    bot.send_message(message.chat.id, "Введи \"/help\", если хочешь увидеть список доступных команд.")


def watch_updates():
    pass


logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

server = Flask(__name__)


@server.route("/" + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://" + APP_NAME + "/" + TOKEN)
    return "!", 200


if __name__ == '__main__':
    server.run(host=HOST, port=PORT)
