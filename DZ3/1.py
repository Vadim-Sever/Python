# Задайте список из нескольких чисел.
# Напишите программу,
# которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях
# элементы 3 и 9, ответ: 12

from random import randint
n = int(input("Укажите количество элементов списка:"))


def fillarray(num):
    list = []
    for i in range(num):
        list.append(randint(0, 10))
    print(list)
    return list


def sumarray(arr):
    arraylength = len(arr)
    sum = 0
    for i in range(arraylength):
        if i % 2 != 0 and i != 0:
            sum = sum+arr[i]
            print("Индекс=", i)
    print(sum)


sumarray(fillarray(n))
