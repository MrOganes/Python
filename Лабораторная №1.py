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