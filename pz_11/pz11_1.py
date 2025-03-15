#Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
#последовательности из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Элементы первого и второго файлов:
#Элементы после сортировки:
#Количество элементов:
#Минимальный элемент кратный 2: 
#Максимальный элемент кратный 5:

a = '-2, 0, 2, 6, 10'
f1 = open('file11_1.txt', 'w')
f1.write(a)
print('элементы первого и второго: ')
print(a)

b = '-1, 1, 3, 7, 15'
f2 = open('file11_2.txt', 'w')
f2.write(b)
print(b)

#стр в список цел чисел
lista = list(map(int, a.split(', ')))
listb = list(map(int, b.split(', ')))

#колво элем 1and2:
c = lista + listb
print('кол-во элементов: ')
print(len(c))

#min and max result
minresult = (min(c)) // 2
maxresult = (max(c)) // 5
print('мин кратное 2: ', minresult)
print('макс кратное 5: ', maxresult)

f3 = open('save11_1.txt', 'w', encoding='utf-8')
#save = f3.write(f1,f2)
#save = f3.write(import print)



f1.close()
f2.close()
f3.close()