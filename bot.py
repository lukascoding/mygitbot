#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import *#Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, RegexHandler, ConversationHandler
from telegram.ext.dispatcher import run_async
from telegram import *#InlineKeyboardButton, InlineKeyboardMarkup, User, Emoji
from emoji import emojize
import logging
import json

from uuid import *
import requests
import arrow
from tld import get_tld
import configparser
import youtube_dl
import datetime
import pytz
import time
import re
import math
import validators
import threading
import ftfy
from tabulate import tabulate
from pprint import pprint
from functions import _Mafia
from helper import _Parser

mafia = None
config = None


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

@run_async
def start(bot, update):
    bot.sendMessage(update.message.chat_id, '/start')

@run_async
def help(bot, update):
    bot.sendMessage(update.message.chat_id, '/help')

@run_async
def test(bot, update):
	print(str(update))
	bot.sendMessage(update.message.chat_id, 'test')

@run_async
def default(bot, update):
	pprint(str(update))
	bot.sendMessage(update.message.chat_id, emojize("{0} :exclamation:".format(update.message.text),use_aliases=True))

@run_async
def inline(bot, update):
    mafia = _Mafia(bot, config)
    query = update.inline_query.query
    results = list()
    parameters = list(_Parser()._parse_parameters(query))
    if len(parameters) in (4, 5):
        try:
            if isinstance(parameters[0], int) and isinstance(parameters[1], str) and (isinstance(parameters[2], float) or isinstance(parameters[2], int)) and ' '.join(map(str, parameters[2:])) in config['Mafia']['Units']:
                results.append(mafia._rent_mercs(parameters[0], parameters[1], parameters[3], ' '.join(map(str, parameters[2:]))))
            else:
                results.append(InlineQueryResultArticle(id=uuid4(), title="Error", input_message_content=InputTextMessageContent(query), description='Invalide input'))
        except:
            results.append(InlineQueryResultArticle(id=uuid4(), title="Error", input_message_content=InputTextMessageContent(query), description='Invalide input'))

    elif len(parameters) in (2, 3):
        try:
            if (isinstance(parameters[0], int) and isinstance(parameters[1], str) and ' '.join(map(str, parameters[1:])) in config['Mafia']['Units']) or (isinstance(parameters[0], float) and isinstance(parameters[1], str) and ' '.join(map(str, parameters[1:])) in config['Mafia']['Units']):
                results.append(mafia._buy_estates(parameters[0], ' '.join(map(str, parameters[1:]))))
            else:
                results.append(InlineQueryResultArticle(id=uuid4(), title="Error", input_message_content=InputTextMessageContent(query), description='Invalide input'))
        except:
            results.append(InlineQueryResultArticle(id=uuid4(), title="Error", input_message_content=InputTextMessageContent(query), description='Invalide input'))
    else:
        results.append(InlineQueryResultArticle(id=uuid4(), title="Error", input_message_content=InputTextMessageContent(query), description='Invalide input'))
    update.inline_query.answer(results)

@run_async
def callback(bot, update):
    query = update.callback_query
    pprint(update)
	#bot.sendMessage(query.message.chat_id, emojize("{0}".format(query.data),use_aliases=True))
		
@run_async
def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    global config
    global mafia
    with open('config.json', 'r') as f:
        config = json.load(f)
        mafia = _Mafia(None, config)
        updater = Updater(config['Bot']['BetaToken'])
        dp = updater.dispatcher
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))
        dp.add_handler(CommandHandler("test", test))
        dp.add_handler(CallbackQueryHandler(callback))
        dp.add_handler(InlineQueryHandler(inline))
        
        dp.add_handler(MessageHandler([Filters.text], default))
        
        #conv_handler = ConversationHandler(
            #entry_points=[CommandHandler('start', start)],

            #states={
                #GENDER: [RegexHandler('^(Boy|Girl|Other)$', gender)],

                #PHOTO: [MessageHandler([Filters.photo], photo),
                        #CommandHandler('skip', skip_photo)],

                #LOCATION: [MessageHandler([Filters.location], location),
                        #CommandHandler('skip', skip_location)],

                #BIO: [MessageHandler([Filters.text], bio)]
            #},

            #fallbacks=[CommandHandler('cancel', cancel)]
        #)
        #dp.add_handler(conv_handler)

        dp.add_error_handler(error)
        
        updater.start_polling()
        updater.idle()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(sys.stderr + '\nExiting by user request.\n')
        sys.exit(0)