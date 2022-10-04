# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt
# в одной строке одно число.
from asyncio.constants import ACCEPT_RETRY_DELAY
from random import randint

n = int(input("Введите число Элементов списка:"))


def filllist(num):
    list = []
    for i in range(num):
        list.append(randint(-num, num))
    print(list)
    return list


array = filllist(n)


def filework(arr):
    z = 1
    array = []
    path = 'file.txt'
    data = open(path, 'r')
    for line in data:
        array.append(int(line))
    print(array)
    data.close()
    return array

array2 = filework(array)

def proizvedenie(arr, index):

    dlina = len(array2)
    i = 0
    itog = 1
    for i in range(dlina):
        itog = array[array2[i]]*itog
    print(itog)

proizvedenie(array,array2)