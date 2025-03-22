#Дана строка 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16',
#отражающая продажи продукции по дням в кг. Преобразовать информацию из
#строки в словари, с использованием функции найти среднее значение продаж по
#каждому виду продукции, результаты вывести на экран.

orange = '45 991 63 100 12'
oranges = [int(x) for x in orange.split(' ')]

def averageo(sumo,longo):
    aver = sumo / longo
    return aver
sumo = sum(oranges)
longo = len(oranges)
resulto = averageo(sumo,longo)

#vtoroe
apple = "13 47 26 0 16"
apples = [int(z) for z in apple.split(' ')]

def averagea(suma,longa):
    avera = suma / longa
    return avera
suma = sum(apples)
longa = len(apples)
resulta = averagea(sumo,longo)

#в словарь
o = {'пнд':oranges[0],'вт':oranges[1],'ср':oranges[2],'чт':oranges[3],'пт':oranges[4]}
a = {'пнд':apples[0],'вт':apples[1],'ср':apples[2],'чт':apples[3],'пт':apples[4]}

print('продажи по дням апельсины: ',o)
print('среднее значение продаж апельсинов: ',resulto)
print('продажи по дням яблоки: ',a)
print('среднее значение продаж яблок: ',resulta)