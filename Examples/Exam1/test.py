from ast import For


f = [1, 2, 3, 4]
print(not 7 in f)

is_odd = f[0] % 2 == 0
print(is_odd)

# //
#a = int(input("a="))
#b = int(input("b="))
# if a > b:
#    print(a)
# else:
# print(b)
# //

list = 1, 2, 3, 4, 5
for i in list:
    print(i**2)
