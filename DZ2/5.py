# Реализуйте алгоритм перемешивания списка.

from random import randint

n = int(input("Введите число элементов списка:"))

#Заполняем


def filllist(num):
    list = []
    for i in range(num):
        list.append(randint(-num, num))
    print(list)
    return list

#перемешиваем


def mixlist(arr):
    newarray = arr[:]
    dlina = len(newarray)
    for i in range(dlina):
        indexrandom = randint(0, dlina-1)
        temp = newarray[i]
        newarray[i] = newarray[indexrandom]
        newarray[indexrandom] = temp
    print(newarray)


mixlist(filllist(n))
