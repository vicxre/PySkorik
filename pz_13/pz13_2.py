#В двумерном списке элементы второго столбца возвести в квадрат.


import random


matric = [[random.randint(1, 10) for x in range(1, 4)] for y in range(random.randint(3, 5))]
print("spisok: ", matric)
answ = []

for i in matric:
    answ += i[1:3][i]



second = spisok[1]
squared = [x ** 2 for x in second]

print(squared)





#map
#pow


