"""
1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
 Пример:
- 6782 -> 23
- 0,56 -> 11

2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
 Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных
позициях. Позиции хранятся в файле file.txt в одной строке одно число.

5. Реализуйте алгоритм перемешивания списка.
"""
import random

# Задача №1
# a = input('Введите число:')
# res = 0
# for i in a:
#     if i.isdecimal():
#         res = int(i) + res
# print(res)

# Задача №2
# number = int(input('Введите число: '))
# res = 1
# mul_result = []
# result = []
# for i in range(1, number + 1):
#     string = ''
#     res = i * res
#     mul_result.append(res)
#     for j in range(1, i + 1):
#         string = string + f"*{str(j)}"
#     result.append(string[1:])
# print(mul_result , result)

# Задача №3
# my_range = int(input('Введите число: '))
#
# my_list = [(1 + 1 / n) ** n for n in range(1, my_range)]
# print(my_list)
# summa = 0
# for value in my_list:
#     summa += value
# print(f'Сумма значений списка: {summa}')

# Задача №4
# n = int(input('Введите число: '))
# rnd_list = [random.randint(-n, n) for _ in range(n)]
# print(rnd_list)  # лист выводится для проверки результата
# mul = 1
# with open('file.txt', 'r') as f:
#     for line in f:  # позиции в файле 0, 1, 2.
#         mul *= rnd_list[int(line)]
# print('Сумма элементов списка по позиция указанных в файл: ', mul)

# Задача #5
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# random.shuffle(my_list)
# print(my_list)
