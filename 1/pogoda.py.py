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


input( )