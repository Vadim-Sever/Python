# Напишите программу, которая найдёт произведение
# пар чисел списка. Парой считаем первый и
# последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint

n = int(input("Введите число Элементов списка:"))


def filllist(num):
    list = []
    for i in range(num):
        list.append(randint(-num, num))
    print(list)
    return list


def proizvedenie(arr):
    arraylength = int(len(arr)/2)
    dlina = len(arr)
    newarray = []
    for i in range(arraylength):
        print(arr[i])
        print(arr[dlina-1])
        # while dlina > int(dlina/2):
        newarray.append(arr[i]*arr[dlina-1])
        dlina = dlina - 1
        print(newarray)

    if (arraylength % 2) != 0:
        print(arr[int(dlina/2)+1])
        newarray.append(arr[int(dlina/2)+1]*arr[int(dlina/2)+1])
    print(newarray)


proizvedenie(filllist(n))
