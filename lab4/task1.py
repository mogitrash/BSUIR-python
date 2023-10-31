class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def perimeter(self):
        return 4 * self.side_length

    def area(self):
        return self.side_length ** 2

    def diagonal(self):
        return self.side_length * (2 ** 0.5)

# Пример использования:
side_length = 5
my_square = Square(side_length)

print("Периметр квадрата:", my_square.perimeter())
print("Площадь квадрата:", my_square.area())
print("Диагональ квадрата:", my_square.diagonal())
