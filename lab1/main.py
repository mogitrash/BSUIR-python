def first():
    n = int(input("Введите натуральное число:"))
    while n <= 0:
        print(input("Неверный ввод"))
        n = int(input("Введите натуральное число:"))
    sum = 0
    
    while n > 0:    
        digit = n % 10
        sum = sum + digit
        n = n // 10
    
    print("Сумма:", sum)

def second():
    slovo = str(input("Введите строку:"))
    a = slovo[::-1]
    if slovo == a:
        print("Строка является палиндромом")
    else:
        print("Строка НЕ является палиндромом")

def third():
    numbers = [2, 4, 6, 8, 10, 12, 14, 16]

    product_of_odd_indices = 1
    for i in range(len(numbers)):
        if i % 2 != 0:
            product_of_odd_indices *= numbers[i]

    print("Произведение элементов с нечетными номерами:", product_of_odd_indices)

    max_element = max(numbers)

    numbers.remove(max_element)

    print("Список без наибольшего элемента:", numbers)

    three_largest_elements = sorted(numbers, reverse=True)[:3]

    print("Три наибольших элемента:", three_largest_elements)
def fourth():
    keys = ['apple', 'banana', 'cherry']
    values = [1, 2, 3]

    result_dict = {}

    for i in range(len(keys)):
        key = keys[i] 
        value = values[i]
        result_dict[key] = value 

    print(result_dict)
def fifth():
    jewelry_store = {
        "Кольцо": ["Золото", 500, 10],
        "Серьги": ["Серебро", 200, 15],
        "Браслет": ["Золото", 800, 5],
        "Ожерелье": ["Платина", 1500, 3]
    }

    def show_description():
        item_name = input("Введите название изделия: ")
        if item_name in jewelry_store:
            description = jewelry_store[item_name][0]
            print(f"{item_name}: {description}")
        else:
            print("Изделие не найдено")

    def show_price():
        item_name = input("Введите название изделия: ")
        if item_name in jewelry_store:
            price = jewelry_store[item_name][1]
            print(f"{item_name}: {price} рублей")
        else:
            print("Изделие не найдено")

    def show_quantity():
        item_name = input("Введите название изделия: ")
        if item_name in jewelry_store:
            quantity = jewelry_store[item_name][2]
            print(f"{item_name}: {quantity} штук")
        else:
            print("Изделие не найдено")

    def show_all_info():
        for item_name, item_info in jewelry_store.items():
            description, price, quantity = item_info
            print(f"{item_name}: {description}, Цена: {price} рублей, Количество: {quantity} штук")

    def purchase():
        total_cost = 0
        while True:
            item_name = input("Введите название изделия (или 'n' для выхода): ")
            if item_name == 'n':
                break
            if item_name in jewelry_store:
                quantity_to_buy = int(input("Введите количество: "))
                if quantity_to_buy <= jewelry_store[item_name][2] and quantity_to_buy >0:
                    price_per_item = jewelry_store[item_name][1]
                    cost = price_per_item * quantity_to_buy
                    total_cost += cost
                    jewelry_store[item_name][2] -= quantity_to_buy
                elif quantity_to_buy <= 0:
                    print("Неверный ввод")
                else:
                    print("Недостаточно товара в магазине.")
            else:
                print("Изделие не найдено")
        print(f"Итоговая стоимость покупки: {total_cost} рублей")

    while True:
        print("\nМеню:")
        print("1. Просмотр описания")
        print("2. Просмотр цены")
        print("3. Просмотр количества")
        print("4. Вся информация")
        print("5. Покупка")
        print("6. До свидания")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            show_description()
        elif choice == '2':
            show_price()
        elif choice == '3':
            show_quantity()
        elif choice == '4':
            show_all_info()
        elif choice == '5':
            purchase()
        elif choice == '6':
            print("До свидания!")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите пункт меню от 1 до 6.")
def sixth():
    import random

    random_numbers = tuple(random.randint(1, 100) for i in range(10))

    max_element = max(random_numbers)
    min_element = min(random_numbers)

    print("Случайные числа:", random_numbers)
    print("Максимальный элемент:", max_element)
    print("Минимальный элемент:", min_element)


choose = int(input("Введите номер задания для выполения:"))
if choose == 1: 
    first()
elif choose == 2:
    second()
elif choose == 3:
    third()
elif choose == 4:
    fourth()
elif choose == 5:
    fifth()
elif choose == 6:
    sixth()
else:
    print("Некорректный выбор. Пожалуйста, выберите пункт меню от 1 до 6.")