# Дана последовательность целых чисел. Поменять местами ее первую и
# последнюю трети.


num = list(range(1, 13))

parts = len(num) // 3


first = num[:parts]
mid = num[parts:-parts]
last = num[-parts:]

new_num = last + mid + first

print(new_num)









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


