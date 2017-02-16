#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from peewee import *
from functions import _Mafia

def create_conifg_json():
    config = {
        'Bot': {
            'Token': '',
            'BetaToken': ''
            },
        'Mafia': {
            'Mercs': {
                'CommandRent': '/rent_{0}_{1}_{2}{3}',
                1: {
                    'Kind': 1,
                    'ForCashPerHour':{
                        'Cost' : 1,
                        'Unit' : 'Mil'
                        },
                    'ForCashPerDay': {
                        'Cost': 22,
                        'Unit': 'Mil'
                        },
                    'ForCashPerWeek': {
                        'Cost': 145,
                        'Unit': 'Mil'
                        },
                    'ForGemsPerDay':{
                        'Cost': 1,
                        'Unit': 'Gems'
                        },
                    'ForGemsPerWeek': {
                        'Cost': 3,
                        'Unit': 'Gems'
                        },
                    'ForGemsPerMonth': {
                        'Cost': 5,
                        'Unit': 'Gems'
                        }},
                2: {
                    'Kind': 2,
                    'ForCashPerHour':{
                        'Cost' : 20,
                        'Unit' : 'Mil'
                        },
                    'ForCashPerDay': {
                        'Cost': 440,
                        'Unit': 'Mil'
                        },
                    'ForCashPerWeek': {
                        'Cost': 2.9,
                        'Unit': 'Bil'
                        },
                    'ForGemsPerDay':{
                        'Cost': 1,
                        'Unit': 'Gems'
                        },
                    'ForGemsPerWeek': {
                        'Cost': 3,
                        'Unit': 'Gems'
                        },
                    'ForGemsPerMonth': {
                        'Cost': 5,
                        'Unit': 'Gems'
                        }},
                3: {
                    'Kind': 3,
                    'ForCashPerHour':{
                        'Cost' : 350,
                        'Unit' : 'Mil'
                        },
                    'ForCashPerDay': {
                        'Cost': 7.7,
                        'Unit': 'Bil'
                        },
                    'ForCashPerWeek': {
                        'Cost': 50.8,
                        'Unit': 'Bil'
                        },
                    'ForGemsPerDay':{
                        'Cost': 1,
                        'Unit': 'Gems'
                        },
                    'ForGemsPerWeek': {
                        'Cost': 3,
                        'Unit': 'Gems'
                        },
                    'ForGemsPerMonth': {
                        'Cost': 5,
                        'Unit': 'Gems'
                        }},
                4: {
                    'Kind': 4,
                    'ForCashPerHour':{
                        'Cost' : 1.2,
                        'Unit' : 'Bil'
                        },
                    'ForCashPerDay': {
                        'Cost': 26.4,
                        'Unit': 'Bil'
                        },
                    'ForCashPerWeek': {
                        'Cost': 174,
                        'Unit': 'Bil'
                        },
                    'ForGemsPerDay':{
                        'Cost': 1,
                        'Unit': 'Gems'
                        },
                    'ForGemsPerWeek': {
                        'Cost': 3,
                        'Unit': 'Gems'
                        },
                    'ForGemsPerMonth': {
                        'Cost': 5,
                        'Unit': 'Gems'
                        }},
                5: {
                    'Kind': 5,
                    'ForCashPerHour':{
                        'Cost' : 5.5,
                        'Unit' : 'Bil'
                        },
                    'ForCashPerDay': {
                        'Cost': 121,
                        'Unit': 'Bil'
                        },
                    'ForCashPerWeek': {
                        'Cost': 797.5,
                        'Unit': 'Bil'
                        },
                    'ForGemsPerDay':{
                        'Cost': 1,
                        'Unit': 'Gems'
                        },
                    'ForGemsPerWeek': {
                        'Cost': 3,
                        'Unit': 'Gems'
                        },
                    'ForGemsPerMonth': {
                        'Cost': 5,
                        'Unit': 'Gems'
                        }}
            },
            'Weaps': {
                'CommandGet': '/get_{0}_{1}{2}',
                'CommandDrop': '/drop_{0}_{1}{2}'
            },
            'Estates': {
                'CommandBuy': '/buy_{0}_{1}{2}',
                'CommandSell': '/sell_{0}_{1}{2}',
                'Toll Road': {
                    'Kind': 'Toll Road',
                    'Code': 'wtr',
                    'Cost': {
                        'Number': 5,
                        'Unit': 'Bil'
                    }
                },
                'Water Pump': {
                    'Kind': 'Water Pump',
                    'Code': 'wwp',
                    'Cost': {
                        'Number': 10,
                        'Unit': 'Bil'
                    }
                },
                'Power Station': {
                    'Kind': 'Power Station',
                    'Code': 'wps',
                    'Cost': {
                        'Number': 15,
                        'Unit': 'Bil'
                    }
                },
                'Railway': {
                    'Kind': 'Railway',
                    'Code': 'wrw',
                    'Cost': {
                        'Number': 25,
                        'Unit': 'Bil'
                    }
                },
                'Military Base': {
                    'Kind': 'Military Base',
                    'Code': 'wwb',
                    'Cost': {
                        'Number': 50,
                        'Unit': 'Bil'
                    }
                }
            },
            'Units':{
                'qrl xq': 1E+30,
                'trl xq': 1E+27,
                'bil xq': 1E+24,
                'mil xq': 1E+21,
                'k xq': 1E+18,
                'qrl': 1E+15,
                'trl': 1E+12,
                'bil': 1E+09,
                'mil': 1E+06,
                'k': 1E+03,
                'one': 1E+00
            }
        }}
    with open('config.json', 'w') as f:
        json.dump(config, f)
#    with open('config.json', 'r') as f:
#    config = json.load(f)
    print(config['Mafia']['Mercs'][1]['ForCashPerWeek']['Cost'])
#    #edit the data
#    config['key3'] = 'value3'
#
#    #write it back to the file
#    with open('config.json', 'w') as f:
#        json.dump(config, f)

def create_db():
    db = SqliteDatabase('bot.db')

    class Messages(Model):
        message_id = IntegerField()
        from_user = TextField()
        date = IntegerField()
        chat = TextField()
        forward_from = TextField()
        forward_from_chat = TextField()
        forward_from_message_id = IntegerField()
        forward_date = IntegerField()
        reply_to_message = TextField()
        edit_date = IntegerField()
        text = TextField()
        entities = TextField()
        audio = TextField()
        document = TextField()
        game = TextField()
        photo = TextField()
        sticker = TextField()
        video = TextField()
        voice = TextField()
        caption = TextField()
        contact = TextField()
        location = TextField()
        venue = TextField()
        new_chat_member = TextField()
        left_chat_member = TextField()
        new_chat_title = TextField()
        new_chat_photo = TextField()
        delete_chat_photo = BooleanField()
        group_chat_created = BooleanField()
        supergroup_chat_created = BooleanField()
        channel_chat_created = BooleanField()
        migrate_to_chat_id = IntegerField()
        migrate_from_chat_id = IntegerField()
        pinned_message = TextField()
        class Mete:
            database = db
    class User(Model):
        user_id = IntegerField()
        class Meta:
            database = db

    db.connect()
    db.create_tables([User, Messages])
    #grandma = Person.select().where(Person.name == 'Grandma L.').get()
    db.close()

#create_conifg_json()
#create_db()
#mafia.getEstates(45, 'qrl xq')
from decimal import Decimal

def format_e(n):
    a = '%E' % n
    return a.split('E')[0].rstrip('0').rstrip('.') + 'E' + a.split('E')[1]



#print(format_e(1000000000000000000000000000000))
#print(format_e(1000000000000000000000000000))
#print(format_e(1000000000000000000000000))
#print(format_e(1000000000000000000000))
#print(format_e(1000000000000000000))
#print(format_e(1000000000000000))
#print(format_e(1000000000000))
#print(format_e(1000000000))
#print(format_e(1000000))
#print(format_e(1000))
#print(format_e(1))

from functions import _Mafia
from helper import _Parser

#with open('config.json', 'r') as f:
#    config = json.load(f)
#    mafia = _Mafia("", config)
#    parser = _Parser()
#    print(mafia._buy_estates(322.4, 'QRL xQ'))
#    print(mafia._rent_mercs(4, 'w', 322.4, 'QRL xQ'))
#    p = list(parser._parse_parameters('1 w 322 QRL xQ'))
#    print(' '.join(map(str, p[3:])).lower())
#    print(type(p[2]))
#    if str(' '.join(map(str, p[3:]))).lower() in config['Mafia']['Units']:
#        print('true')
#    if len(p) in (4, 5):
#        try:
#            if isinstance(p[0], int) and isinstance(p[1], str) and (isinstance(p[2], float) or isinstance(p[2], int)) and ' '.join(map(str, p[2:])) in config['Mafia']['Units']:
#                print('true')
#        except:
#            print('false')
#
#    elif len(p) in (2, 3):
#        try:
#            if type(p[0]) == int and type(p[1]) == str and type(p[2]) == float and ' '.join(map(str, p[2:])) in config['Mafia']['Units']:
#                print('true')
#        except:
#            print('false')
#    else:
#        print('ok')

import sqlite3

#conn = sqlite3.connect('bot.db')
#conn.execute('''INSERT INTO user (user_id) VALUES (1);''')
#conn.commit()
#conn.close()

from peewee import *

db = SqliteDatabase('bot.db')

class user(Model):
    id = IntegerField(primary_key= True, null = False),
    user_id = IntegerField(null = False, unique = True),
    lang = TextField(default='en')
    class Meta:
        database = db

db.connect()

test = user(id=2,user_id=8,lang='hi')
test.save()

for user in user.select():
    print(str(user.user_id))