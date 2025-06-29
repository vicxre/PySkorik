#1
import random as r
from idlelib import replace


visota = int(input('ввеидте высоту матрицы ->'))
shirina = int(input('ввеидте ширину матрицы ->'))

matr1 = [[r.randint(1,10) for _ in range(shirina)] for _ in range(visota)]
print('матрица №1 do', matr1)


matr2 = [[r.randint(1,10) for _ in range(3)] for _ in range(3)]
print('матрица №2 do', matr2)

zamena = replace.matr1(matr2)
print(zamena)




