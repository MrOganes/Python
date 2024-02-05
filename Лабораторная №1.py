#Элизбаров Оганес, группа 37/1, вариант-3

#Задание 1

#функция 1
def prost(x):
    """Проверяет, является ли число простым."""
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def max_prost_del(x):
    """Находит максимальный простой делитель числа."""
    max = 1
    for i in range(2, x+1):
        if x % i == 0 and prost(i):
            max = i
    return max

#функция 2
def proizv(number):
    """Находит произведение цифр числа, не делящихся на 5."""
    proizv = 1
    while(number):
        if((number%10)%5!=0):
            proizv*=number%10
        number//=10
    return proizv

#функция 3
def prost(x):
    """Проверяет, является ли число простым."""
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def max_del(x):
    """Находит максимальный, нечетный, непростой делитель числа."""
    for i in range(x, 0, -1):
        if(x%i==0 and i%2!=0 and not prost(i)):
            return i
    return 1

def proizv(number):
    """Находит произведение цифр числа."""
    proizv = 1
    while(number):
        proizv*=number%10
        number//=10
    return proizv

def NOD(a,b):
    for i in range(min(a,b), 0, -1):
        if(a%i==0 and b%i==0):
            return i
    return 1

#Задание 2

import random as rd
def random_words(str):
    words = str.split()
    rd.shuffle(words)
    new_str = ' '.join(words)
    return new_str

#Задание 3
def kol_slov(str):
    words = str.split()
    kol = 0
    for i in words:
        if(len(i)%2==0):
            kol+=1
    return kol

#Задание 4
def sort(colors):
    color_order = {"белый": 0, "синий": 1, "красный": 2}
    for i in range(0, len(colors)-1):
        for j in range(i+1, len(colors)):
            if(color_order[colors[i]]>color_order[colors[j]]):
                colors[i], colors[j] = colors[j], colors[i]
    return colors

colors = ["красный", "белый", "синий", "красный", "белый", "синий"]

#Задание 5

import re
def find_dates(str):
    pattern = r'\b\d{1,2}\s(?:января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)\s\d{4}\b'
    dates = re.findall(pattern, str)
    return dates

#Задание 6




#Задание 7
#Задание 8
#Задание 9
#Задание 10
#Задание 11
#Задание 12
#Задание 13
#Задание 14
#Задание 15
#Задание 16
#Задание 17
#Задание 18
#Задание 19