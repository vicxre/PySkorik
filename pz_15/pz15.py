#Приложение ПЛАТНАЯ ПОЛИКЛИНИКА для некоторой организации. БД
#должна содержать таблицу Пациент со следующей структурой записи: ФИО пациента,
#ФИО врача, диагноз, стоимость лечение.

import sqlite3 as sq

with sq.connect('bolnica.db') as conn:
    cursor = conn.cursor()

    #таблица пациенты
    cursor.execute(
        """ CREATE TABLE IF NOT EXISTS patients 
        ( id INTEGER PRIMARY KEY AUTOINCREMENT, 
        full_name TEXT, 
        doctor_full_name TEXT, 
        diagnosis TEXT, 
        treatment_cost REAL ) """)

data_to_insert = [
    ('Иванов Сергей', 'Антонов Олег', 'Грипп', 1500.0),
    ('Смирнова Ирина', 'Корнеева Марина', 'Отит', 2500.0),
    ('Кузнецов Павел', 'Степанова Елена', 'Аппендицит', 8000.0),
    ('Николаева Юлия', 'Романов Антон', 'Аллергия', 1000.0),
    ('Волков Александр', 'Шарапова Татьяна', 'Холецистит', 4000.0),
    ('Андреева Дарья', 'Егоров Николай', 'Фарингит', 1200.0),
    ('Максимов Денис', 'Соколова Светлана', 'Бронхит', 3000.0),
    ('Федорова Екатерина', 'Новиков Максим', 'Гастрит', 2000.0),
    ('Орлов Константин', 'Борисова Анна', 'Простуда', 1800.0),
    ('Петров Артем', 'Миронова Виктория', 'Артроз', 6000.0)
]

with sq.connect('bolnica.db') as conn:
    cursor = conn.cursor()
    cursor.executemany(
        "INSERT INTO patients(full_name, "
        "doctor_full_name, "
        "diagnosis, "
        "treatment_cost) VALUES(?, ?, ?, ?)",
        data_to_insert)


#поиск where
def search_by_criteria():
    with sq.connect('bolnica.db') as conn:
        cursor = conn.cursor()

        #все пациенты с диагнозом грипп
        cursor.execute("SELECT * FROM patients WHERE diagnosis = 'Грипп'")
        results = cursor.fetchall()
        if len(results):
            for row in results:
                print(row)
        else:
            print("Нет результатов.")

        #все пациенты, лечившихся у доктора Антонов Олега
        cursor.execute("SELECT * FROM patients WHERE doctor_full_name = 'Антонов Олег'")
        results = cursor.fetchall()
        if len(results):
            for row in results:
                print(row)
        else:
            print("Нет результатов.")

        #все пациенты с ценой лечения больше 3000
        cursor.execute("SELECT * FROM patients WHERE treatment_cost > 3000")
        results = cursor.fetchall()
        if len(results):
            for row in results:
                print(row)
        else:
            print("Нет результатов.")
search_by_criteria()


#удаление delete и where
def delete_data():
    with sq.connect('bolnica.db') as conn:
        cursor = conn.cursor()

        #удаление запись с ID = 1
        cursor.execute("DELETE FROM patients WHERE id = 1")

        #удаление всех кто с диагнозом аллергия
        cursor.execute("DELETE FROM patients WHERE diagnosis = 'Аллергия'")

        #удаление всех кто лечился у Шараповой Татьяны
        cursor.execute("DELETE FROM patients WHERE doctor_full_name = 'Шарапова Татьяна'")
delete_data()


#редакт update и where
def update_data():
    with sq.connect('bolnica.db') as conn:
        cursor = conn.cursor()

        # Пример 1: Изменяем цену лечения пациента с ID = 2 на 2200
        cursor.execute("UPDATE patients SET treatment_cost = 2200 WHERE id = 2")

        # Пример 2: Меняем врачу пациенту Смирновой Ирине
        cursor.execute("UPDATE patients SET doctor_full_name = 'Иванченко Андрей' WHERE full_name = 'Смирнова Ирина'")

        # Пример 3: Обновляем диагноз пациента Петров Артем
        cursor.execute("UPDATE patients SET diagnosis = 'Артрит' WHERE full_name = 'Петров Артем'")
update_data()