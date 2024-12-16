#Описать функцию DigitCountSum(K, C, S), находящую количество C цифр целого
#положительного числа K, а также их сумму S (K — входной, C и S — выходные
#параметры целого типа). С помощью этой функции найти количество и сумму цифр
#для каждого из пяти данных целых чисел.

try:
    K = int(input("введите число: "))

    if K < 0:
        print("не по понятиям уважаемый")
    else:

        def DigitCountSum(K):

            digits = list(str(K))

            S = 0

            C = len(str(K))

            print(C)

            for i in range (C):
                S += int(digits [i])

            print(S)

        DigitCountSum(K)

except ValueError:
    print("что-то пошло не так ")