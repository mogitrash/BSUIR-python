def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_prime_by_index(index):
    prime_count = 0
    num = 2
    while True:
        if is_prime(num):
            prime_count += 1
            if prime_count == index:
                return num
        num += 1



def find_min_key(input_data):
    if not input_data:
        return None
    min_key = min(input_data, key=input_data.get)
    return min_key

def process_list(input_data):
    zero_indices = [i for i, x in enumerate(input_data) if x == 0]
    if len(zero_indices) >= 2:
        product = 1
        for i in range(zero_indices[0], zero_indices[1]):
            product *= input_data[i]
        unique_elements = list(set(input_data))
        return product, unique_elements
    else:
        return "Not enough zero elements in the list."

def process_number(input_data):

    divisors = [i for i in range(1, input_data + 1) if input_data % i == 0]
    return divisors

def process_string(input_data):
    input_data = input_data.lower()
    reversed_input = input_data[::-1]
    vowel_count = sum(1 for char in input_data if char in 'aeiouаеёиоуыэюя')
    consonant_count = len(input_data) - vowel_count
    return input_data == reversed_input, vowel_count, consonant_count

def matrix_row_sum(matrix):
    row_sums = [sum(row) for row in matrix]
    return row_sums

def main():
    while True:
        print("\nВыберите действие:")
        print("1. Найти простое число по номеру")
        print("2. Найти минимальный ключ в словаре или произведение нулевых элементов в списке")
        print("3. Найти сумму каждой строки матрицы")
        print("4. Проверить работу try/except/finally")
        print("0. Выйти")
        
        choice = input("Введите номер действия: ")
        
        if choice == "1":
            try:
                index = int(input("Введите номер простого числа: "))
                if index < 1:
                    print("Номер должен быть больше 0.")
                else:
                    result = find_prime_by_index(index)
                    print(f"Простое число под номером {index} равно {result}")
            except ValueError:
                print("Введите корректный номер.")
        
        elif choice == "2":
            input_data = eval(input("Введите данные (словарь, список, число или строку): "))
            if isinstance(input_data, dict):
                min_key = find_min_key(input_data)
                print(f"Минимальный ключ в словаре: {min_key}")
                break;
            elif isinstance(input_data, list):
                list_product, unique_elements = process_list(input_data)
                print(f"Произведение нулевых элементов в списке: {list_product}")
                print(f"Уникальные элементы в списке: {unique_elements}")
                break;
            elif isinstance(input_data, int):
                divisors = process_number(input_data)
                print(f"Делители числа: {divisors}")
                break;
            elif isinstance(input_data, str):
                is_palindrome, vowel_count, consonant_count = process_string(input_data)
                print(f"Палиндром: {is_palindrome}")
                print(f"Количество гласных: {vowel_count}")
                print(f"Количество согласных: {consonant_count}")
                break;

            
            
        elif choice == "3":
            try:
                m = int(input("Введите количество строк матрицы: "))
                n = int(input("Введите количество столбцов матрицы: "))
                matrix = []
                for i in range(m):
                    row = [int(x) for x in input(f"Введите {n} элементов для строки {i+1}: ").split()]
                    matrix.append(row)
                row_sums = matrix_row_sum(matrix)
                for i, row_sum in enumerate(row_sums):
                    print(f"Сумма элементов в строке {i+1}: {row_sum}")
            except ValueError:
                print("Введите корректное число строк и столбцов.")
        
        elif choice == "4":
            try:
                num = int(input("Введите число для деления: "))
                result = 10 / num
                print(f"Результат деления 10 на {num}: {result}")
            except ZeroDivisionError:
                print("Деление на ноль невозможно.")
            except ValueError:
                print("Введите корректное число.")
            finally:
                print("Программа завершена.")
        
        elif choice == "0":
            print("Выход из программы.")
            break
        
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие из списка.")

if __name__ == "__main__":
    main()
