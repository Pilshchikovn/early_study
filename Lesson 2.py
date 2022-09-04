N = 6
a = [0] * N
for i in range(N):
    a[i] = i ** 2
print(a)


a = [x ** 3 for x in range(N)]
print(a)


d = input('Введите числа через пробел ')
a = (int(x) for x in d.split())
print(list(a))


d = [-1, -2, 3, 4, 5, 6, 7, 8, 9, 10]
chet = ['chetnoe' if x % 2 == 0 else 'nechetnoe'
        for x in d
        if x > 0
        ]
print(chet)

a = [f'{i}*{j} = {i * j}'
     for i in range(10)
     for j in range(10)
     ]
print(a)

M, N = 3, 4
matrix = [[a for a in range(M)] for b in range(N)]
print(matrix)

A = [[1, 2, 3], [4, 5, 6]]
a = [[x ** 2 for x in row] for row in A]
print(a)
