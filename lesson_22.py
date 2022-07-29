# matrix  = [[2, -5, -11, 0],
#            [-9, 4, 6, 13],
#            [4, 7, 12, -2]]
#
# print(matrix[1][2])  # вывод элемента на позиции (2, 3)

# rows, cols = 3, 4           # rows - количество строк, cols - количество столбцов
# matrix  = [[2, 3, 1, 0],
#            [9, 4, 6, 8],
#            [4, 7, 2, 7]]
# for r in range(rows):
#     for c in range(cols):
#         print(matrix[r][c], end=' ')
#     print()

# rows, cols = 3, 4                # rows - количество строк, cols - количество столбцов
# matrix  = [[277, -930, 11, 0],
#            [9, 43, 6, 87],
#            [4456, 8, 290, 7]]
#
# for r in range(rows):
#     for c in range(cols):
#         print(str(matrix[r][c]).ljust(6), end='')
#     print()


# rows, cols = 3, 4           # rows - количество строк, cols - количество столбцов
# matrix  = [[2, 3, 1, 0],
#            [9, 4, 6, 8],
#            [4, 7, 2, 7]]
# for c in range(cols):
#     for r in range(rows):
#         print(matrix[r][c], end=' ')
#     print()

# def print_matrix(matrix, n, width=1):
#     for r in range(n):
#         for c in range(n):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()
#
# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
#
# print_matrix(matrix, 2)

# s=[[input() for _ in range(m)] for _ in range(n)]
# print

# n = 3
# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# for i in range(n):
#     for j in range(n):
#         print(a[3 - 0 - 1][3 - 1 - 1], end=' ')
#     print()

# n,m, matrix= int(input()),int(input()),[]
# s=[[input() for i in range(m)] for j in range(n)]
# print(*s, sep='\n')
#
# n = int(input())
# m = int(input())
# [print(*[input() for i in range(m)]) for i in range(n)]

