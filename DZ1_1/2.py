# Напишите программу для. проверки истинности
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.

# заполняем массив
def FillArray(x):
    name = ["x", "y", "z"]
    inputarray = []
    for i in range(x):
        inputarray.append(input(f"Введите значение {name[i]}: "))
    return inputarray


res = FillArray(3)

# не(x или Y или Z) = не x и не Y и не Z


def Proverka(res):
    z = not (res[0] or res[1] or res[2])
    p = not res[0] and not res[1] and not res[2]
    if z == p:
        result = True
    else:
        result = False
    return result


if Proverka(res) == True:
    print(f"True")
else:
    print(f"False")
