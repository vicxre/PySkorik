#В исходном текстовом файле(Dostoevsky.txt) найти все произведения писателя.
#Посчитать количество полученных элементов.


import re


def find(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()


    pattern = r'(?:«|")([А-ЯЁ][А-Яа-яё\s\-—:]+?(?:\s*\([^)]+\))?)(?:»|")'
    works = re.findall(pattern, text)

    #удаляем дубликаты, сохраняя порядок
    seen = set()
    unique_works = [work for work in works if not (work in seen or seen.add(work))]

    return unique_works


filename = 'Dostoevsky.txt'

try:
    works = find(filename)

    print("произведения")
    for i, work in enumerate(works, 1):
        print(f"{i}. {work}")

    print(f"\nвсего произведений: {len(works)}")

except FileNotFoundError:
    print("ошибка!!!")



