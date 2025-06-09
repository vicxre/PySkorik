#Создайте класс "Машина" с атрибутами "марка", "модель" и "год выпуска".
#Напишите метод, который выводит информацию о машине в формате "Марка:
#марка, Модель: модель, Год выпуска: год".

class machine:

    def __init__(self, brand, model, years):
        self.brand = brand
        self.model = model
        self.years = years

    def inform(self):

        car = machine('bmw', 'm5 f90', '2023')

        print(f'brand:{self.brand},model:{self.model},year of release:{self.years}')




