#Создайте класс "Автомобиль", который содержит информацию о марке, модели и
#годе выпуска. Создайте класс "Грузовик", который наследуется от класса
#"Автомобиль" и содержит информацию о грузоподъемности. Создайте класс
#"Легковой автомобиль", который наследуется от класса "Автомобиль" и содержит
#информацию о количестве пассажиров.

class car:
    def __init__(self, brand, model, release):
        self.brand = brand
        self.model = model
        self.release = release

        def inform(self):
            return f"марка: {self,brand}, модель: {self.model}, год выпуска: {self.release}"


class truck(car):
    def __inir__(self, brand, model, release, weight_up):
        super().__init__(brand, model, release)
        self.weight_up = weight_up

    def inform(self):
        info = super().inform()
        return f"{info}, грузоподъемность в тоннах: {self.weight_up}"


class easycar(car):
    def __init__(self, brand, model, release, passenger_num):
        super().__init__(brand, model, release)
        self.passenger_num = passenger_num

    def inform(self):
        base_info = super().inform()
        return f'{base_info}, кол-во пассажиров: {self.passenger_num}'



