# Дана последовательность целых чисел. Поменять местами ее первую и
# последнюю трети.

num = list(range(1, 10))

def zamena(num):

    parts = len(num) // 3
    return (lambda seq, t: seq[2*t:] + seq[t:2*t] + seq[:t])(num, parts)

result = zamena(num)
print('до: ', num,'после: ',result)










#tret = len(num) // 3

#zamena = tret.replace[[0],[2]]

#print(zamena)

#for zamena in num:
 #   print(zamena)

#zamena = tret.replace(num)


#from functools import reduce


#zamena = tret.replace([0],[2])

#print(zamena)


#tret = [num in num//3 for num]


