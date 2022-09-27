# print('hello')

import string


value = None
print(type(value))
a = 1
b = 'привет'
print(a, b)
print('{}-{}-{}'.format(a, b, b))
print('{2}-{1}-{0}'.format(a, b, b))
print(f'{a}-{b}-{b}')
f = False
print(f)
#list = ['1', '2', '3', 'hello', 1, 2]
# print(list)

print('input text')
key = input()
print(type(key))

print("input numeric")
z = int(input())
print(type(z))

# print(type(key))
# fadsg
if type(z) != int:
    (print('Введите число'))
else:
    print("z число")
#

if type(key) != str:
    (print('Введите текст'))
else:
    print("key текст")
