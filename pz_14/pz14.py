#В исходном текстовом файле(Dostoevsky.txt) найти все произведения писателя.
#Посчитать количество полученных элементов.

import re


f1 = open('Dostoevsky.txt', 'r', encoding='utf-8')
txt = f1.read()

pattern = r'(?i)(?:роман|повесть|рассказ|опубл\.?)([^a-zA-Z]*([А-ЯЁ][\w\s]+))'
works = re.findall(pattern, txt)
unique_titles = set(works)


count_unique_titles = len(unique_titles)

for title in unique_titles:
    print(title)

print('кол-во произведений:', count_unique_titles)









