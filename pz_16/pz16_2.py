#Создайте класс "Автомобиль", который содержит информацию о марке, модели и
#годе выпуска. Создайте класс "Грузовик", который наследуется от класса
#"Автомобиль" и содержит информацию о грузоподъемности. Создайте класс
#"Легковой автомобиль", который наследуется от класса "Автомобиль" и содержит
#информацию о количестве пассажиров.

#bibika
class car:

    def __init__(self, brand, model, years):
        self.brand = brand
        self.model = model
        self.years = years

    def car(self):

        return f'brand:{self.brand},model:{self.model},year of release:{self.years}'


#gruzovik
class truck(car):

    def __init__(self, brand, model, years, gruzo):
        super().__init__(brand, model, years)
        self.gruzo = gruzo






tachila = car(' bmw ', ' m5f90 ', ' 2023. ')
massa = truck('8тонн')