#Даны координаты поля шахматной доски х, у (целые числа, лежащие в диапазоне 1-8.
# Учитывая, что левое нижнее поле доски (1,1) является черным,
# проверить истинность высказывания: Данное поле является белым.

X = int(input("Введите целое число лежащее в диапозоне от 1 до 8 x:"))
Y = int(input("Введите целое число лежащее в диапозоне от 1 до 8 y:"))

try:

    #условие
    if X < 1 or X > 8 or Y < 1 or Y > 8:

        print("Введите не меньше 1 и не больше 8")

    else:
        if (X + Y) % 2 == 0:
            print("Нет, черное")

        else:
            print("Да, белое")

except ValueError:
    print("Что-то пошло не так")