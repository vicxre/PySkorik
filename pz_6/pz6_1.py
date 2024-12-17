#Дан целочисленный список размера N. Проверить, чередуются ли в нем четные и
#нечетные числа. Если чередуются, то вывести 0, если нет, то вывести порядковый
#номер первого элемента, нарушающего закономерность.


# random для пяти чисел
a1, a2, a3, a4, a5 = (random.randint(1, 99), random.randint(1, 99),
                      random.randint(1, 99), random.randint(1, 99),
                      random.randint(1, 99))

# до пропуска через саму функцию
print(a1, a2, a3, a4, a5)

a1 = DigitCountSum(a1)
a2 = DigitCountSum(a2)
a3 = DigitCountSum(a3)
a4 = DigitCountSum(a4)
a5 = DigitCountSum(a5)

