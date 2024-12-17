#Описать функцию DigitCountSum(K, C, S), находящую количество C цифр целого
#положительного числа K, а также их сумму S (K — входной, C и S — выходные
#параметры целого типа). С помощью этой функции найти количество и сумму цифр
#для каждого из пяти данных целых чисел.

import random

try:
    K = int(input("введите число: "))

    if K < 0:
        print("не по понятиям уважаемый")
    else:

        def DigitCountSum(K):

            digits = list(str(K))

            S = 0

            C = len(str(K))

            print(C, " - длина числа")

            #вводит в список
            for i in range (C):
                S += int(digits [i])

            print(S, ' - сумма цифр числа')

            #рандом пяти случайных чисел
            numbers = [random.randint(1, 99) for i in range(5)]

            #обработка каждого рандом числа
            for num in numbers:
                C, S = DigitCountSum(num)
                print(f"Для числа", num, 'количество цифр', C , "сумма цифр", S)


        DigitCountSum(K)

except ValueError:
    print("что-то пошло не так ")