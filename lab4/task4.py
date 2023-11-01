class Car:
    # Поле класса, общее для всех автомобилей
    car_count = 0

    def __init__(self, make, model, year, fuel_type):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_type = fuel_type
        self.mileage = 0  # Пробег в милях
        Car.car_count += 1

    # Метод экземпляра, увеличивающий пробег
    def drive(self, miles):
        self.mileage += miles

    # Метод экземпляра, выводящий информацию об автомобиле
    def car_info(self):
        return f"{self.year} {self.make} {self.model} ({self.fuel_type}), Пробег: {self.mileage} миль"

    # Статический метод для конвертации миль в километры
    @staticmethod
    def miles_to_kilometers(miles):
        return miles * 1.60934

    # Метод класса, выводящий общее количество созданных автомобилей
    @classmethod
    def get_total_car_count(cls):
        return cls.car_count

# Пример использования:
car1 = Car("Toyota", "Camry", 2022, "бензин")
car2 = Car("Honda", "Civic", 2021, "гибрид")

car1.drive(100)
car2.drive(150)

print(car1.car_info())  # Вывод информации о первом автомобиле
print(car2.car_info())  # Вывод информации о втором автомобиле

# Использование статического метода
miles = 100
kilometers = Car.miles_to_kilometers(miles)
print(f"{miles} миль = {kilometers} километров")

# Использование метода класса
total_car_count = Car.get_total_car_count()
print(f"Общее количество автомобилей: {total_car_count}")
