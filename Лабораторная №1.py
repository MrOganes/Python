#Элизбаров Оганес, группа 37/1, вариант-3

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
