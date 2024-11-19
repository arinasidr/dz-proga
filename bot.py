import telebot
from telebot import types

KEY_API = '7483581690:AAHdz2MqT-YLZ7ZCfLQf8__D7SfSH0zq714'

class Response:
    requests = 0
    group_name = ''
    school_lang = ''
    work_python = ''

responses = {}

bot = telebot.TeleBot(KEY_API)

@bot.message_handler(commands = ['start'])
def start_message(message):
    print('start: ' + message.text)
    responses[message.chat.id] = Response()
    responses[message.chat.id].requests = 1
    bot.send_message(message.chat.id, 'привет! скажи свое имя)')

@bot.message_handler(content_types = ['text'])
def text_message(message):
    if responses[message.chat.id].requests == 1:
        responses[message.chat.id].group_name = message.text
        responses[message.chat.id].requests == 2
        bot.send_message(message.chat.id, 'какой язык программирования изучал(а) в школе?')
    elif responses[message.chat.id].requests == 2:
        responses[message.chat.id].school_lang = message.text
        responses[message.chat.id].requests == 3
        bot.send_message(message.chat.id, 'имел(а) ли опыт работы с питоном? (0, 1, 2, 3, ....)')
    else:
        bot.send_message(message.chat.id, 'твои ответы очень важны, спасибо!')
        bot.send_message(message.chat.id, 'твои ответы очень важны, спасибо!')
    

bot.infinity_polling()