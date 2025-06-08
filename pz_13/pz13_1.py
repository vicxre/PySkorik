#В двумерном списке найти сумму элементов второй половины матрицы.

import random


matric = [[random.randint(1, 10) for x in range(1, 5)] for y in range(random.randint(3, 4))]
print("spisok: ", matric)
answ = []

for i in matric:
    answ += i[1:3][i]


print(sum(str(answ[1])))
