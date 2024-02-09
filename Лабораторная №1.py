#Элизбаров Оганес, группа 37/1

#Задание 1

#функция 1

def prost(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def max_prost_del(x):
    max = 1
    for i in range(2, x+1):
        if x % i == 0 and prost(i):
            max = i
    return max

#функция 2

def proizv(number):
    proizv = 1
    while(number):
        if((number%10)%5!=0):
            proizv*=number%10
        number//=10
    return proizv

#функция 3

def prost(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def max_del(x):
    for i in range(x, 0, -1):
        if(x%i==0 and i%2!=0 and not prost(i)):
            return i
    return 1

def proizv(number):
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

def find_rus_char(str):
    count = 0
    for char in str:
        if(("а"<=char and char<="я")or("А"<=char and char<="Я")):
            count+=1
    return count

#Задание 7

def find_rus_lower_char(str):
    chars = []
    for char in str:
        if("а" <= char and char <= "я"):
            chars.append(char)
    return chars

#Задание 8

def find_min_integer(str):
    integers = re.findall(r'-?\b\d+\b', str)
    min = int(integers[0])
    print(integers)
    for i in integers:
        if int(i)<min:
            min = int(i)
    return min

#Задание 9

strings = []
str = input()
while(str):
    strings.append(str)
    str = input()
for i in range(0, len(strings)-1):
    for j in range(i+1, len(strings)):
        if(len(strings[i])>len(strings[j])):
            strings[i], strings[j] = strings[j], strings[i]

#Задание 10

strings = []
str = input()
while(str):
    strings.append(str)
    str = input()
for i in range(0, len(strings)-1):
    for j in range(i+1, len(strings)):
        if(len(strings[i].split())>len(strings[j].split())):
            strings[i], strings[j] = strings[j], strings[i]