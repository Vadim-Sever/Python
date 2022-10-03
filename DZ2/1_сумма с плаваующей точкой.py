# Напишите программу, которая принимает на вход вещественное
# число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

x = input("Введите вещественное число X= \n")
razmer = len(x)


def str_to_num(str):
    str = str.strip()  # првоеряет наличие пробелов в начале и коне строки
    if '.' in str and str.replace('.', '').isdigit():
        return float(str)
    elif str.isdigit():  # Метод isdigit() возвращает True, если все символы в строке являются цифрами. Если нет, возвращается False.
        return int(str)


def FillArray(arr):
    Array = []
    for i in arr:
        z = str_to_num(i)
        if z is not None:
            Array.append(str_to_num(i))
    print(Array)
    print(sum(Array))


FillArray(x)
