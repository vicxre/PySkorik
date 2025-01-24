#Дана строка 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16',
#отражающая продажи продукции по дням в кг. Преобразовать информацию из
#строки в словари, с использованием функции найти среднее значение продаж по
#каждому виду продукции, результаты вывести на экран.

def averageO(sum_orange,long_orange):

    orange = {}
    int.inf = "45 991 63 100 12"
    inf = int.inf.split()
    orange['MONDAY'] = inf[0]
    orange['TUESDAY'] = inf[1]
    orange['WEDNESDAY'] = inf[2]
    orange['THURSDAY'] = inf[3]
    orange['FRIDAY'] = inf[4]

    sum_orange = sum(inf)
    long_orange = len(inf)
    average_orange = sum_orange / long_orange
    return average_orange

averageO(sum_orange,long_orange)
resultO = average_orange
print(resultO)



apple = {}
int.inf = "13 47 26 0 16"
inf = int.inf.split()
apple['MONDAY'] = inf[0]
apple['TUESDAY'] = inf[1]
apple['WEDNESDAY'] = inf[2]
apple['THURSDAY'] = inf[3]
apple['FRIDAY'] = inf[4]
print('Яблоки продажи с пнд до пт - ',apple)







