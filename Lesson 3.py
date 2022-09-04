# a = {'dfdg': 1, 'rwefw': 2}
# s = {key.upper(): int(value) for key, value in a.items()}
# print(s)

d = [1,2,5,-7,-43,'325','0']
c = {int(x) for x in d if int(x) > 0}
print(c)