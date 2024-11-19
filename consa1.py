from math import *
#1
# a = 11
# b = 10
# if a <= b:
#     a = 0
# print(a, b)

#2
# a = -2
# b = 4
# c = 8
# if a > 0:
#     a = a**2
# if b > 0:
#     b = b**2
# if c > 0:
#     c = c**2
# print(a, b, c)

#3
# a = input("Введите положительное целое число: ")
# c = 0
# for i in a:
#     if i in '0123456789':
#         c += int(i)
#     else:
#         print('Неправильный ввод числа, попробуйте еще раз!')
#         c = 0
#         break
# print(c)

#4
# a = 1
# b = 2
# c = 5
# if 1 < a < 3:
#     print(a)
# if 1 < b < 3:
#     print(b)
# if 1 < c < 3:
#     print(c)

#5
# next = 0
# while True:
#     current = int(input("Введите целое число: "))
#     if current < next:
#         break
#     next = current
# print("Ввод прерван")

#6
# x = 10
# n = input('1 – возвести число в квадрат; 2 – извлечь корень квадратный; 3 – вычислить синус; 4 – косинус ')
# for i in n:
#     if i == '1':
#         x = x**2
#     if i == '2':
#         x = x**0.5
#     if i == '3':
#         x = sin(x)
#     if i == '4':
#         x = cos(x)
# print(x)

#7
# k = int(input('Введите цифру: '))
# for i in range(1, 11):
#     print(f'{k} * {i} = ' + str(i*k))

#8
# s = input('введите символ в нижнем регистре от a до f: ')
# if s in ['a', 'b', 'c', 'd', 'e', 'f']:
#     print(s.upper())
# else:
#     print('неправильный ввод(')

#9
# a = 10
# b = 8
# c = 6
# d = 2
# if a <= b <= c <= d:
#     a, b, c, d = max(a, b, c, d), max(a, b, c, d), max(a, b, c, d), max(a, b, c, d),
# elif a > b > c > d:
#    pass
# else:
#     a = a**2
#     b = b**2
#     c = c**2
#     d = d**2
# print(a, b, c, d)

#10
# m = int(input('Введите длину прямоугольника: '))
# n = int(input('Введите ширину прямоугольника: '))
# for i in range(1, n + 1):
#     print('1' * m)

#11
# a = int(input('Введите целое число: '))
# b = int(input('Введите целое число: '))
# z = float(input('Введите действительное число: '))
# if a % b == 0:
#     print(z *  (a % b))
# else:
#     print(z /  (a % b))

#12
# s = input('введите числовую последовательность: ')
# for i in range(1, len(s) -1):
#     a, b, c = int(s[i-1]), int(s[i]), int(s[i+1])
#     if a < b and c < b and b%2 == 0:
#         print('существует четный по значению локальный максимум - ' + str(b))
    
#13
# n = int(input("Введите количество чисел: "))
# s = [int(input(f"Введите число {i+1}: ")) for i in range(n)]
# lst = []
# c = 0
# for j in s:
#     if j % 5 == 0 and j % 7 != 0:
#         lst.append(j)
#         c += j
# print('количество: ' + str(len(lst)))
# print('сумма: ' + str(sum(lst)))

#14
# n = int(input("Введите количество чисел: "))
# s = [int(input(f"Введите число {i+1}: ")) for i in range(n)]
# c = 0
# for j in s:
#     if j > 0:
#         c += j
# print(c * 2)

#15
# n = int(input("Введите количество чисел: "))
# s = [int(input(f"Введите число {i+1}: ")) for i in range(n)]
# p = 1
# for j in s:
#     if j % 7 == 0:
#         p *= j
# print(p)

#16 a
# a = float(input('введите действительное число: '))
# if -2 <= a < 2:
#     print(f'f({a}) = ' + str(a**2))
# else:
#     print(f'f({a}) = 4')

#16 b
# a = int(input('введите действительное число: '))
# if  a <= 2:
#     print(f'f({a}) = ' + str(a**2 + 4*a + 5))
# else:
#     print(f'f({a}) = ' + str(1 / (a**2 + 4*a + 5)))

#17
# a = int(input('введите действительное число: '))
# n = int(input('Введите натуральное число: '))
#a
# print(a**n)
# #b
# p = 1
# for i in range(0, n):
#     p *= (a + i)
# print(p)
#c
# s = 0
# tek = 1
# for i in range(0, n + 1):
#     tek = tek / (a + i)
#     s += tek
# print(s)

#18
# i = int(input("Введите натуральное число i: ")) - 1 
# n = int(input("Введите натуральное число n >= i: "))

# numbers = []
# for j in range(n):
#     num = float(input(f"Введите число {j + 1}: "))
#     numbers.append(num)

# print(numbers)

# s = 0
# c = 0
# for k in range(n):
#     if k != i:
#         s += numbers[k]
#         c += 1
    
# if c > 0:
#     print(s/c)

#19 (пример остроугольного треуг: 5, 6, 7)
# x = float(input('Введите 1 сторону треугольника: '))
# y = float(input('Введите 2 сторону треугольника: '))
# z = float(input('Введите 3 сторону треугольника: '))
# if (x < y + z) and (y < x + z) and (z < x + y):
#     print('да, существует')
#     if (x**2 + y**2 > z**2) and (x**2 + z**2 > y**2) and (z**2 + y**2 > x**2):
#         print('он остроугольный')
#     else: 
#         print('он не остроугольный')
# else:
#     print('нет, не существует')

#20
# x = float(input('Введите 1 действительное число: '))
# y = float(input('Введите 2 действительное другое число: '))
# z = float(input('Введите 3 действительное другое число: '))
# if x < y and x < z:
#     x = (y + z) / 2
# elif y < x and y < z:
#     y = (x + z) / 2
# elif z < y and z < x:
#     z = (z + z) / 2
# else:
#     if x < y:
#         x = (y + z) / 2
#     else:
#         y = (x + z) / 2
# print(x, y, z)

#21
# a = float(input('Введите 1 действительное число не равное 0: '))
# b = float(input('Введите 2 действительное число: '))
# c = float(input('Введите 3 действительное число: '))
# if a == 0:
#     print('неправильный ввод')
# else:
#     d = b**2 - 4*a*c
#     if d >= 0:
#         x1 = (-b + d**0.5) / (2*a)
#         x2 = (-b - d**0.5) / (2*a)
#         print(f'уравнение имеет действительные корни: {x1}, {x2}')
#     else:
#         print('уравнение не имеет действительных корней')

#22
# a = int(input('введите целое положительное число: '))
# print(bin(a)[2:])