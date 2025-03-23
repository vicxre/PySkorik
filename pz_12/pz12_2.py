#Составить генератор (yield), который выводит из строки только цифры.

from unicodedata import digit

num = '13vc27holymoly'

def numbers(num):


    for n in num:
        if num.isdigit():
            yield



#yield from [x for x in num.isdigit()]
#print(numbers)

