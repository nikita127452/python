from datetime import datetime
from random import choices
import requests

print("Hello my Freinds")
hello = input("")
if hello =="hi":
    print("What’s up?")
else:
    print("Ебать ты даун тебя что не наулили здороваться")    
    print("What’s up?")
how_are_you = input("") 
if how_are_you == "нормально" :
    print ("Very god")
elif how_are_you == "плохо" :
    print("Может я могу чем то помочь ")
    bad = input("")
    if bad == "нет" :
        print('Если что-то понадобиться то я всегда здесь')
    elif bad == "да" :
        print("Чем могу помочь")
elif how_are_you == "отлично" :
    print("Ну это очень хорошо")
elif how_are_you == "хорошо" :
    print("Ну так это замечательно")
else:
    print("ЗАЕБАЛ пиши нормально")
for t in reversed(range(4)):
    p = input("Введите пароль:")
    if p == "loki" :
        print('Пароль верный, вход выполнен')
        print("Приветствую мой повелитель") 
        print("можете написать \"menu \" если хотите узныть возможности ")               
        menu = input("")
        if menu == "menu" :
            print("Что я могу? попробуй такие коианды как \"время\", \"погода\", \"рандомайзер\", \"шутки\"")
            choice = input("")
            if choice == "time":
                current_datetime = datetime.now()
                print(current_datetime)
            elif choice =="weather" : 
                from ctypes.wintypes import LANGID
                from pyowm import OWM
                from pyowm.utils import config
                from pyowm.utils import timestamps

                owm = OWM('c27e6538c35597a24685a29e20a92852', )
                mgr = owm.weather_manager()

                place = input("В каком ты городе: " )

                observation = mgr.weather_at_place('place')
                w = observation.weather

                temp = w.temperature('celsius')["temp"]

                print( "В городе " + place + " сейчас " + w.detailed_status  )
                print( "Температура сейчас в районе " + str(temp))

                if temp < 10:
                    print( "Сейчас холодно можешь идти гулять в танковой броне")
                elif  temp < 20:
                    print( "болле мение нормально но одевайся тепло" )
                elif temp < 0 :
                    print( "Еба ты даун выходить в такую погоду" )
                else:
                    print( "Тепло" )
            elif choice == "joke":
                print("Nikita dibil didn't teach me jokes XD")
            elif choice == "random":
                import random
                print("Вудите число:")
                randoms = input(" ")
                print(random.randint(0, randoms))
               

        elif menu == "time":
                current_datetime = datetime.now()
                print(current_datetime)
        elif menu =="weather" : 
            from ctypes.wintypes import LANGID
            from pyowm import OWM
            from pyowm.utils import config
            from pyowm.utils import timestamps

            owm = OWM('c27e6538c35597a24685a29e20a92852', )
            mgr = owm.weather_manager()

            place = input("В каком ты городе: " )

            observation = mgr.weather_at_place('place')
            w = observation.weather

            temp = w.temperature('celsius')["temp"]

            print( "В городе " + place + " сейчас " + w.detailed_status  )
            print( "Температура сейчас в районе " + str(temp))

            if temp < 10:
                    print( "Сейчас холодно можешь идти гулять в танковой броне")
            elif  temp < 20:
                    print( "болле мение нормально но одевайся тепло" )
            elif temp < 0 :
                    print( "Еба ты даун выходить в такую погоду" )
            else:
                    print( "Тепло" )

        elif menu == "joke":
                print("Nikita dibil didn't teach me jokes XD")
        
        else:
            print("error")
        break
    print('Неправильный пароль, осталось попыток :', t)
input( )    