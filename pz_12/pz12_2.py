#Составить генератор (yield), который выводит из строки только цифры.



num = input('ПИШИ-->')


def search(num):

    for non in num:
        if non.isdigit():
            yield non

for numbers in search(num):
    print(numbers)
