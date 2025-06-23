#В двумерном списке элементы второго столбца возвести в квадрат.

import random as r



matrix = [[r.randint(1, 10) for _ in range(3)] for _ in range(3)]
print("исходная: ", matrix)


for new in matrix:
    new[1] *= new[1]

#перебор циклом для вывода всех трех списков
print('матрица после возведения в квадрат:')
for new in matrix:
    print(new)