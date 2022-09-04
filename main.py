"""
1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
 Пример:
- 6782 -> 23
- 0,56 -> 11

2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
 Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
"""


# Задача №1
# a = input('Введите число:')
# res = 0
# for i in a:
#     if i.isdecimal():
#         res = int(i) + res
# print(res)

def insert_char(string, chr):
    ret = ''
    for k in string:
        ret += k + chr
    return ret[:-1]


number = int(input('Введите число: '))
res = 1
mul_result = []
result = []
for i in range(1, number + 1):
    string = ''
    res = i * res
    mul_result.append(res)
    for j in range(1, i + 1):
        string = string + str(j)
    new_string = insert_char(string, '*')
    result.append(new_string)
print(mul_result , result)
