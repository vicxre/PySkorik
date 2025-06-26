#В двумерном списке элементы второго столбца возвести в квадрат.

import random as r

visota = int(input('высота:'))
shirina = int(input('ширина:'))
matrix = [[r.randint(1, 10) for _ in range(shirina)] for _ in range(visota)]
print("исходная: ", matrix)

for new in matrix:
    new[1] *= new[1]

print('матрица после возведения в квадрат:')
for new in matrix:
    print(new)