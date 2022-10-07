# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной
# части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from pickletools import floatnl
from random import uniform

n = int(input("Введите число Элементов списка:"))


def filllist(num):
    list = []
    for i in range(num):
        list.append(round(uniform(1.5, 6.7), 2))
    print(list)
    return list


def minmax(arr):
    arraylength = len(arr)
    min = arr[0]
    max = arr[0]
    for i in range(arraylength):
        if arr[i] < min:
            min = arr[i]
        if arr[i] > max:
            max = arr[i]
    print("Max=", max, "Min=", min)
    maxfloat = int(max) - max
    print(maxfloat)
    minfloat = int(min) - min
    print(minfloat)
    print(round(maxfloat-minfloat, 2))


minmax(filllist(n))
