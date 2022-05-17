#int
from traceback import print_tb


number = 5
#float
fnumber = 5.7
#string
name = "Nikita"
#bool
statys = True

# Вывод на екран
print( name)

#Экранирование
print( "Он \"плохой\" человек" )
print('Он "плохой "человек')

#Перевод строки
print("Привет")
print("Мир")
print('Привет \nмир')

#Конкатенация
print("Привет меня зовут " + name)
print("Мне " + str(number) + " года")

name_n2 = input("Ведите свое имя" )
age = input("Укажите свой возраст" )

print( "Привет, " + name_n2 + "!" )
print( "Тебе уже"+ age + " года" )

#+ - * / ** %...
a = 5
b = 10
c = a + b
print( c )