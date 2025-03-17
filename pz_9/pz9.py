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




#def averageO():
    # Данные о количестве апельсинов каждый день недели
 #   n = "45 991 63 100 12"

    # Преобразуем строку в список целых чисел
  #  numbers = list(map(int, n.split()))

    # Создадим словарь с днями недели и количеством апельсинов
   # orange = {
    #    'MONDAY': numbers[0],
     #   'TUESDAY': numbers[1],
      #  'WEDNESDAY': numbers[2],
       # 'THURSDAY': numbers[3],
        #'FRIDAY': numbers[4]
    #}

    # Суммируем количество апельсинов за всю неделю
#   sum_orange = sum(numbers)

    # Определяем длину списка (количество дней)
    #long_orange = len(numbers)

    # Вычисляем среднее количество апельсинов в день
    #average_orange = sum_orange / long_orange


    #return average_orange
    #return orange


# Вызов функции и вывод результата
#resultO = averageO()
#print(resultO)
#print(orange)


