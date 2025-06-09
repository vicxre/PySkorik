#Создайте класс "Машина" с атрибутами "марка", "модель" и "год выпуска".
#Напишите метод, который выводит информацию о машине в формате "Марка:
#марка, Модель: модель, Год выпуска: год".

class car:

    def __init__(self, brand, model, years):
        self.brand = brand
        self.model = model
        self.years = years

    def car(self):

        print(f'brand:{self.brand},model:{self.model},year of release:{self.years}')


tachila = car(' bmw ', ' m5f90 ', ' 2023. ')

tachila.car()



