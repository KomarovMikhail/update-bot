# -*- coding: utf-8 -*-
from config import *
import telebot
from flask import Flask, request
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta


bot = telebot.TeleBot(TOKEN)

scheduler = BackgroundScheduler()
scheduler.start()


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    main_markup = main_menu_button()
    text = 'Приветствую! С помощью этого бота ты можешь отслеживать расписание докладов и заводить новые знакомства.'
    bot.send_message(message.chat.id, text, reply_markup=main_markup)

    text = 'Что я могу для тебя сделать?'
    inline_markup = generate_menu()
    bot.send_message(message.chat.id, text, reply_markup=inline_markup)


@bot.message_handler(content_types=["text"])
def unknown_messages(message):
    bot.send_message(message.chat.id, "Извини, я тебя не понимаю. Попробуй еще раз.")


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
