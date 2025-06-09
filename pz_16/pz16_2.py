#Создайте класс "Автомобиль", который содержит информацию о марке, модели и
#годе выпуска. Создайте класс "Грузовик", который наследуется от класса
#"Автомобиль" и содержит информацию о грузоподъемности. Создайте класс
#"Легковой автомобиль", который наследуется от класса "Автомобиль" и содержит
#информацию о количестве пассажиров.

#bibika
class car:

    def __init__(self, brand, model, years, gruz, kolvo):
        self.brand = brand
        self.model = model
        self.years = years

    def inform(self):




#gruzovik
class truck(car):

    def infa(self, gruz):
        self.gruz = 0






tachila = car('bmw', 'm5 f90', '2023')
massa = truck('8тонн')