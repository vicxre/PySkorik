#Дана строка 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16',
#отражающая продажи продукции по дням в кг. Преобразовать информацию из
#строки в словари, с использованием функции найти среднее значение продаж по
#каждому виду продукции, результаты вывести на экран.
def averageO(sum_orange,long_orange):

    orange = {}
    int.n = "45 991 63 100 12"
    n = int.split()
    orange['MONDAY'] = n[0]
    orange['TUESDAY'] = n[1]
    orange['WEDNESDAY'] = n[2]
    orange['THURSDAY'] = n[3]
    orange['FRIDAY'] = n[4]

    sum_orange = sum(n)
    long_orange = len(n)
    average_orange = sum_orange / long_orange
    return average_orange

print(average0)
print(orange)


apple = {}
int.inf = "13 47 26 0 16"
inf = int.inf.split()
apple['MONDAY'] = inf[0]
apple['TUESDAY'] = inf[1]
apple['WEDNESDAY'] = inf[2]
apple['THURSDAY'] = inf[3]
apple['FRIDAY'] = inf[4]
print('Яблоки продажи с пнд до пт - ',apple)







