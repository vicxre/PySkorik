#Приложение ПЛАТНАЯ ПОЛИКЛИНИКА для некоторой организации. БД
#должна содержать таблицу Пациент со следующей структурой записи: ФИО пациента,
#ФИО врача, диагноз, стоимость лечение.

import sqlite3 as sq

# Создание базы данных и таблицы Пациент
with sq.connect("polyclinic.db") as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS patients (
    patient_id INTEGER PRIMARY KEY NOT NULL,
    patient_name VARCHAR(50) NOT NULL,
    doctor_name VARCHAR(50) NOT NULL,
    diagnosis TEXT,
    treatment_cost DECIMAL(10, 2) NOT NULL
    )""")

#вывести все строчки, где стоимость лечения больше 5000
with sq.connect("polyclinic.db") as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM patients WHERE treatment_cost > 5000")
    result = cur.fetchall()
    print("Пациенты с стоимостью лечения больше 5000:", result)

#вывести информацию о пациентах конкретного врача
with sq.connect("polyclinic.db") as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM patients WHERE doctor_name = 'Иванова'")
    result1 = cur.fetchone()
    result2 = cur.fetchmany(2)
    print("Первый пациент врача Иванова:", result1)
    print("Следующие два пациента врача Иванова:", result2)