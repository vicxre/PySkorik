#В двумерном списке найти сумму элементов второй половины матрицы.

import random as r



matrix = [[r.randint(1, 10) for _ in range(4)] for _ in range(4)]


#вторая половина
polovina = len(matrix) // 2

sum_matr = sum(sum(non) for non in matrix[polovina:])

print('исходная матрица:',matrix, 'сложение второй половины: ',sum_matr)