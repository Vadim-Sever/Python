# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

x = int(input("Введите число"))

# определяю счетчиком сколько едениц в данном числе
def shetdlina(arr):
    res = 0
    for i in range(arr):
        res = res+1
    return res

# определяю произведение предшестсующих числе в данном числе 
def proizvedenie(arr):
    z = 1
    for i in range(arr):
        if i > 0:
            z = z*i
    return z


# print(proizvedenie(x))

# exit()


def FillArray(arr):
    array = []
    z = 0
    for i in range(arr+1):
        if i > 0:
            if shetdlina(i) == 1:
                array.append(i)
            else:
                i = shetdlina(i)*proizvedenie(i)
                array.append(i)
        print(array)


FillArray(x)
