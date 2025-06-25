#В исходном текстовом файле(Dostoevsky.txt) найти все произведения писателя.
#Посчитать количество полученных элементов.

import re


f1 = open('Dostoevsky.txt', 'r', encoding='utf-8')

txt =f1.read()

#composition