#Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
#последовательности из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Элементы первого и второго файлов:
#Элементы после сортировки:
#Количество элементов:
#Минимальный элемент кратный 2: 
#Максимальный элемент кратный 5:

a = (0,2,6,10,-2)
f1 = open('file11_1_1.txt', 'w')
f1.write(str(a))

b = (1,3,7,15,-1)
f2 = open('file11_1_2.txt', 'w')
f2.write(str(b))
print('элементы первого и второго: ', a,b)

sorta =  sorted(a)
sortb = sorted(b)
print('сортировка a : ',sorta)
print('сортировка b : ',sortb)

c = sorta + sortb
kolvo = (len(c))
print('кол-во элементов: ',kolvo)

minresult = (min(c)) // 2
maxresult = (max(c)) // 5
print('мин кратное 2: ', minresult)
print('макс кратное 5: ', maxresult)

f3 = open('save11_1.txt', 'w', encoding='utf-8')
f3.write(str(sorta))
f3.write(str(sortb))
f3.write(str(minresult))
f3.write(str(maxresult))

f1.close()
f2.close()
f3.close()