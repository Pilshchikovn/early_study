# from fractions import Fraction as F
#
# numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14',
#            '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02',
#            '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31',
#            '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']
#
# for num in numbers:
#     print(f"{num} = {F(num)}")
#
# from fractions import Fraction
#
# s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'
#
# s = str(s).split()
# print(Fraction(min(s)) + Fraction(max(s)))

# from fractions import Fraction
#
# a = int(input())
# b = int(input())
#
# print(Fraction(a, b))

# from math import gcd
# from fractions import Fraction
# n = int(input())
# result = []
# while n != 1:
#     for i in range(1, n):
#         if gcd(i, n) == 1:
#             result.append(f'{i}/{n}')
#     n -= 1
# answer = sorted(map(Fraction, result))
# print(*answer, sep='\n')

import turtle
import turtle as t

t.colormode(255)
t.bgcolor('black')
t.speed(10)
t.penup()
t.shape('turtle')
r = 0
g = 0
b = 255
for i in range(1, 1000):
    if 0 < i % 379 < 64:
        r += 4
    elif 63 < i % 379 < 127:
        b -= 4
    elif 126 < i % 379 < 190:
        g += 4
    elif 189 < i % 379 < 253:
        r -= 4
    elif 252 < i % 379 < 316:
        b += 4
    elif 315 < i % 379 < 379:
        g -= 4
    t.color((0, 0, 0), (r, g, b))
    t.stamp()
    t.left(22)
    t.forward(1.01 ** i)

t.mainloop()