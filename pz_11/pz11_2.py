#Из предложенного текстового файла (text18-25.txt) вывести на экран его содержимое,
#количество символов, принадлежащих к группе букв. Сформировать новый файл, в
#который поместить текст в стихотворной форме предварительно удалив букву «с» из
#текста.

f1 =
f1 = open('text18-25.txt')
for line in f1:
 print(line, remove('c','С'))
print(type(f1.read()))
f1.close()



