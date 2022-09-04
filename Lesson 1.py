a = [[2], [3], [4]]
b = [[5], [6], [7]]
c = []
for i, row in enumerate(a):
    r = []
    for j, x in enumerate(row):
        r.append(x + b[i][j])
    c.append(r)

print(c)

t = ['Скажи ка дядя ведь не  даром',
     'Москва спаленноая  пожаром',
     'Французам  отдана'
     ]
for i, line in enumerate(t):
    while line.count('  '):
        line = line.replace('  ', ' ')
    t[i] = line
print(t)



m, n = list(map(int, input('Введите n и m: ').split()))
zeros = []
for i in range(m):
    zeros.append([0]*n)
print(zeros)

for i in range(m):
    for j in range(n):
        zeros[i][j] =1
print(zeros)

