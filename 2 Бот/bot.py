import telebot

from ctypes.wintypes import LANGID
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('c27e6538c35597a24685a29e20a92852', )
mgr = owm.weather_manager()


bot = telebot.TeleBot("5362579911:AAEdgyrnPclsp4CTA2AGRyZXePYHRRVj3V4", parse_mode=None)

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = mgr.weather_at_place( message.text )
    w = observation.weather
    temp = w.temperature('celsius')["temp"]

    answer = "В городе " + message.text + " сейчас " + w.detailed_status  + "\n"
    answer += "Температура сейчас в районе " + str(temp) + "\n\n"

    if temp < 10:
        answer += "Сейчас холодно можешь идти гулять в танковой броне"
    elif  temp < 20:
        answer += "болле мение нормально но одевайся тепло" 
    elif temp < 0 :
        answer += "Еба ты даун выходить в такую погоду" 
    else:
        answer +=  "Тепло"   

    bot.send_message(message.chat.id, answer )

bot.polling( none_stop = True)