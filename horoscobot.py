# -*- encoding: utf-8 -*-

import telepot
from pprint import pprint
import time
import random
import string
import sys

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('invitadobot.log', 'a', encoding='utf8')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

def log_message(msg):
    _from = msg.get('from', {})
    username = _from.get('username')
    usr_id = _from.get('id')
    first_name = _from.get('first_name')
    text = msg.get('text')
    text = ' '.join(text.split()) if text else text

    chat_id = msg['chat']['id']

    if msg['chat']['type'] in ('group', 'supergroup'):
      title = msg['chat']['title']
    else:
      title = 'None'

    logger.info(u"<{}>#{} {}#{} <{}>: {}".format(title, chat_id, username, usr_id, first_name, text))


name = "horoscothebot"

signos = ['aries',
          'tauro',
	      'geminis',
          'cancer',
          'acuario',
          'piscis',
          'leo',
          'virgo',
          'libra',
          'escorpio',
          'sagitario',
          'capricornio']

predicciones = dict()
for signo in signos:
	with open('signos/' + signo + '.txt') as f:
		predicciones[signo] = f.readlines()


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    flavor = telepot.flavor(msg)

    log_message(msg)

    if flavor != 'chat':
        return

    if 'text' in msg:
        text = msg['text']
        signo = text[1:].split("@")[0]
        if signo in signos:
            bot.sendChatAction(chat_id, "typing")
            m = "*%s*\n%s" % (signo.capitalize().decode('utf-8'), predicciones[signo][0].decode('utf-8'))
            bot.sendMessage(chat_id, m, parse_mode="Markdown")

token = sys.argv[1]
bot = telepot.Bot(token)

print 'Listening ...'
bot.message_loop(handle)

while 1:
    time.sleep(10)
