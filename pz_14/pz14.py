#В исходном текстовом файле(Dostoevsky.txt) найти все произведения писателя.
#Посчитать количество полученных элементов.
import re

def find(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    pattern = r'(?:«|")([А-ЯЁ][А-Яа-яё\s\-—:]+?(?:\s*\([^)]+\))?)(?:»|")'
    works = re.findall(pattern, text)

    #удаление повторок и сохранение порядка
    seen = set()
    unique_works = [work for work in works if not (work in seen or seen.add(work))]
    return unique_works

filename = 'Dostoevsky.txt'
print("произведения:")
works = find(filename)

try:
    for i, work in enumerate(works, 1):
        print(i, work)

    print('всего произведений:', len(works))

except FileNotFoundError:
    print("ошибочка!!!")



