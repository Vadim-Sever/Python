# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


min = -8
max = 8


def fibonachi(num):
    if num == -2:
        res = -1
    if num == 1 or num == 2 or num == -1:
        res = 1
    if num < -2:
        if num % 2 != 0:
            num = num*-1
            res = fibonachi(num+2)-fibonachi(num+1)
        else:
            res = fibonachi(num+2)-fibonachi(num+1)
    if num > 2:
        res = fibonachi(num-1)+fibonachi(num-2)
    return res


def perebor(nummin, nummax):
    i = nummin
    while i >= nummin and i < 0:
        res = fibonachi(i)
        print("Число Фибонначи при i=", i, "= ", res)
        i += 1
    i = 1
    while i <= nummax and i > 0:
        res = fibonachi(i)
        print("Число Фибонначи при i=", i, "= ", res)
        i += 1


perebor(min, max)
