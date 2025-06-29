#ввод диапозона рандома
import random as r




try:
    ot = int(input('введи от скольки будет рандом ->'))
    do = int(input('введи до скольки будет рандом ->'))

    result = r.randint(ot,do)

    print('результат рандома -> ', result)

except ValueError:
    print("nefiga!!!")
    print('введи цифарки')
