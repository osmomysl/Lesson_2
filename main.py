# Домашнее задание к Занятию 2.

# Задачи на циклы и оператор условия------
# ----------------------------------------

"""
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
"""
print('Задача 1')

for i in range(1, 6):
    print(i, '{:010}'.format(0), sep='. ')

print()

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
print('Задача 2')

five = 0
for i in range(1, 11):
    print('(', i, sep='', end='/10) ')
    num = int(input('Введите любую цифру: '))  # int - обязательно!
    if num == 5:
        five += 1
print('Количество введённых цифр "пять":', five)
print()

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
print('Задача 3')

sum = 0
for i in range(0, 101):
    sum += i  # sum = sum + i
print('Сумма ряда чисел от 1 до 100:', sum)

print()

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
print('Задача 4')

fact = 1
for i in range(2, 11):
    fact *= i
if fact == 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10:  # проверка
    print('Произведение ряда чисел от 1 до 10:', fact)
else:
    print('Error')

print()

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''
print('Задача 5')

''' Вариант 1 '''
# a = input('Введите целое число любой разрядности: ')
# b = len(a)
# for i in range(0, b):
#     print(a[i])

''' Вариант 2 '''
# a = input('Введите целое число любой разрядности: ')
# b = len(a)
# i = 0
# while i < b:
#     print(a[i])
#     i += 1

''' Вариант 3 '''
import math

a = int(input('Введите целое число любой разрядности: '))
while a > 0:
    lg = int(math.log10(a))
    print(a // 10 ** lg)
    a = a % 10 ** lg

print()

'''
Задача 6
Найти сумму цифр числа.
'''
print('Задача 6')

num = int(input('Введите целое число любой разрядности: '))
sum = 0
while num > 0:
    sum += num % 10
    num //= 10
print('Сумма цифр числа:', sum)

print()

'''
Задача 7
Найти произведение цифр числа.
'''
print('Задача 7')

num = int(input('Введите целое число любой разрядности: '))
mult = 1
while num > 0:
    mult *= num % 10
    num //= 10
print('Произведение цифр числа:', mult)

print()

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
print('Задача 8')

num = int(input('Введите целое число любой разрядности: '))
while num > 0:
    if num % 10 == 5:
        print('Есть ли среди цифр числа 5: ', 'да')
        break
    num //= 10
else:
    print('Есть ли среди цифр числа 5: ', 'нет')

print()

'''
Задача 9
Найти максимальную цифру в числе
'''
print('Задача 9')

num = int(input('Введите целое число любой разрядности: '))
max = 0
while num > 0:
    if max < num % 10:
        max = num % 10
    elif max == 9:
        break
    num //= 10
print('Максимальная цифра в числе:', max)

print()

'''
Задача 10
Найти количество цифр 5 в числе
'''
print('Задача 10')

num = int(input('Введите целое число любой разрядности: '))
five = 0
while num > 0:
    if num % 10 == 5:
        five += 1
    num //= 10
print('Количество цифр 5 в числе:', five)
