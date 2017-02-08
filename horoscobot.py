# -*- encoding: utf-8 -*-

import telepot
from pprint import pprint
import time
import random
import string
import sys

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
    pprint(msg)
    pprint("flavor " + flavor)

    if flavor != 'chat':
        return

    if 'text' in msg:
        text = msg['text']

        if "@" + name in text:
            tokens = text.split()
            for token in tokens:
                signo = token.lower()
                if signo in signos:
                    bot.sendChatAction(chat_id, "typing")
                    m = "*%s*\n%s" % (signo.capitalize().decode('utf-8'), predicciones[signo][0].decode('utf-8'))
                    bot.sendMessage(chat_id, m, parse_mode="Markdown")
                    break
        else:
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
