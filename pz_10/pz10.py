def averageO():
    # Данные о количестве апельсинов каждый день недели
    n = "45 991 63 100 12"

    # Преобразуем строку в список целых чисел
    numbers = list(map(int, n.split()))

    # Создадим словарь с днями недели и количеством апельсинов
    orange = {
        'MONDAY': numbers[0],
        'TUESDAY': numbers[1],
        'WEDNESDAY': numbers[2],
        'THURSDAY': numbers[3],
        'FRIDAY': numbers[4]
    }

    # Суммируем количество апельсинов за всю неделю
    sum_orange = sum(numbers)

    # Определяем длину списка (количество дней)
    long_orange = len(numbers)

    # Вычисляем среднее количество апельсинов в день
    average_orange = sum_orange / long_orange


    return average_orange
    return orange


# Вызов функции и вывод результата
resultO = averageO()
print(resultO)
print(orange)