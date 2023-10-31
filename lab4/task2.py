class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки с помощью ручки '{self.title}'")

class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки с помощью карандаша '{self.title}'")

class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки с помощью маркера '{self.title}'")

# Создание экземпляров классов и вызов метода draw
pen = Pen("Гелевая ручка")
pencil = Pencil("Черный карандаш")
marker = Handle("Тонкий маркер")

pen.draw()  # Вывод: Запуск отрисовки с помощью ручки 'Гелевая ручка'
pencil.draw()  # Вывод: Запуск отрисовки с помощью карандаша 'Черный карандаш'
marker.draw()  # Вывод: Запуск отрисовки с помощью маркера 'Тонкий маркер'
