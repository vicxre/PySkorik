#Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
#последовательности из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:

#Элементы первого и второго файлов:
#Элементы после сортировки:
#Количество элементов:
#Минимальный элемент кратный 2: 
#Максимальный элемент кратный 5:

#1file
a = '-2, 0, 2, 6, 10'
f1 = open('file11_1.txt', 'w')
f1.write(a)
print('Элементы первого и второго файлов: ')
print(a)

#2file
b = '-1, 1, 3, 7, 15'
f2 = open('file11_2.txt', 'w')
f2.write(b)
print(b)

#стр в список цел. чисел
lista = list(map(int, a.split(', ')))
listb = list(map(int, b.split(', ')))

#Количество элементов 1and2:
c = lista + listb
print('Количество элементов: ')
print(len(c))

#min and max result
minresult = (min(c)) // 2
maxresult = (max(c)) // 5
print('минимальное кратное двум: ', minresult)
print('максимальное кратное пяти: ', maxresult)


