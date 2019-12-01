from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# PROXY = {'proxy_url': 'socks5://t2.learn.python.ru:1080',
#     'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

import logging
import ephem
import datetime
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = 'вызван старт'
    print (text)
    update.message.reply_text(text)
    
def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def planet (bot,update):
    print('planet')
    user_text = update.message.text.split()
    print(user_text)
    update.message.reply_text(user_text[1])
    user_text[1]=user_text[1].lower()
    
    if user_text[1] == 'mercury':
        m = ephem.Mercury(datetime.datetime.now())
        
    elif user_text[1] == 'venus':
        m = ephem.Venus(datetime.datetime.now())
        
    elif user_text[1] == 'mars':
        m = ephem.Mars(datetime.datetime.now())
        
    elif user_text[1] == 'jupiter':
        m = ephem.Jupiter(datetime.datetime.now())
        
    elif user_text[1] == 'saturn':
        m = ephem.Saturn(datetime.datetime.now())
        
    elif user_text[1] == 'uranus':
        m = ephem.Uranus(datetime.datetime.now())
        
    elif user_text[1] == 'neptune':
        m = ephem.Neptune(datetime.datetime.now())
        
    print(ephem.constellation(m))
    update.message.reply_text(ephem.constellation(m))


def main():
    mybot = Updater("949706218:AAGj9-tlVSLt367pKMFxeQmFNQXaiHIY1UI")
    #, request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()


main()