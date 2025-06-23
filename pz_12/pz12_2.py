#Составить генератор (yield), который выводит из строки только цифры.

from unicodedata import digit


num = int(input('ПИШИ-->'))

def numbers(num):
    for i in num:

        if num.isdigit():

            yield num
















#filter = [num for num in numbers if num = '123456789']

#   for n in num:
  #      if num.isdigit():
   #         yield



#print(numbers)

