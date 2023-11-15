import numpy as np
import matplotlib.pyplot as plt

# Заданные значения
c_min = -10
c_max = 1
delta_c = 0.5
x_value = 12.1

# Функция f(x)
def f(x, c):
    return pow(pow(abs(2*x - c), 3), 1/5) + 0.567

# Создаем массив значений функции f(x)
c_values = np.arange(c_min, c_max + delta_c, delta_c)
f_values = [f(x_value, c) for c in c_values]

# Выводим на экран значения аргумента и значения функции
print("Значения аргумента (c):", c_values)
print("Значения функции (f(x)):", f_values)

# Находим наибольшее, наименьшее, среднее значение
max_value = np.max(f_values)
min_value = np.min(f_values)
mean_value = np.mean(f_values)

# Выводим результаты
print("\nНаибольшее значение функции:", max_value)
print("Наименьшее значение функции:", min_value)
print("Среднее значение функции:", mean_value)
print("Количество элементов массива:", len(f_values))

# Сортируем массив
sorted_f_values = np.sort(f_values)[::-1]

# Выводим отсортированный массив
print("\nОтсортированный массив (по возрастанию):", sorted_f_values)

# Строим график функции
plt.plot(c_values, f_values, label='f(x)')
plt.axhline(y=mean_value, color='r', linestyle='--', label='Среднее значение f(x)')

# Оформляем график
plt.xlabel('Значения аргумента (c)')
plt.ylabel('Значения функции (f(x))')
plt.title('График функции f(x)')
plt.legend()

# Выводим график на экран
plt.show()
