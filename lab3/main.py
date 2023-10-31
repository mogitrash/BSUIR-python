import os
import json

def read_data_from_user():
    data = []
    while True:
        line = input("Введите строку (пустая строка для завершения ввода): ")
        if not line:
            break
        data.append(line)
    with open("F1.txt", "w") as file:
        file.write("\n".join(data))

def copy_lines_without_digits():
    with open("F1.txt", "r") as f1, open("F2.txt", "w") as f2:
        for line in f1:
            if not any(char.isdigit() for char in line):
                f2.write(line)

def count_lines_starting_with_A():
    with open("F2.txt", "r") as file:
        lines = file.readlines()
        count = sum(1 for line in lines if line.strip().startswith('A'))
        print(f"Количество строк, начинающихся на 'А' в файле F2: {count}")

def replace_english_numbers_with_russian():
    numbers = {
        "One": "Один",
        "Two": "Два",
        "Three": "Три",
        "Four": "Четыре"
    }

    with open("english_numbers.txt", "r", encoding="utf-8") as english_file, open("russian_numbers.txt", "w", encoding="utf-8") as russian_file:
        for line in english_file:
            # разделяем строку на слова
            words = line.split()
            #создаем список для замененных слов
            replaced_words = []
            for word in words:
                # если слово есть в словаре,заменяем его
                if word in numbers:
                    replaced_words.append(numbers[word])
                else:
                    replaced_words.append(word)
            #собираем строку снова и записываем в новый файл
            russian_line = " ".join(replaced_words)
            russian_file.write(russian_line + "\n")


def get_russian_number(english_number):
    numbers = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    return numbers.get(english_number, english_number)

def create_subjects_dict():
    subjects_dict = {}

    with open("subjects.txt", "r", encoding="utf-8") as file:
        for line in file:
            parts = line.split(":")
            subject_name = parts[0].strip()
            hours = parts[1].split()
            total_hours = 0

            for hour in hours:
                if hour.endswith("(л)"):
                    total_hours += int(hour.replace("(л)", ""))
                elif hour.endswith("(пр)"):
                    total_hours += int(hour.replace("(пр)", ""))
                elif hour.endswith("(лаб)"):
                    total_hours += int(hour.replace("(лаб)", ""))
            
            subjects_dict[subject_name] = total_hours

    print(subjects_dict)

def calculate_and_save_company_data():
    companies = []
    with open("companies.txt", "r") as file:
        for line in file:
            parts = line.split()
            name, form, revenue, expenses = parts[0], parts[1], int(parts[2]), int(parts[3])
            profit = revenue - expenses
            companies.append({name: profit})
    
    profitable_companies = [company for company in companies if list(company.values())[0] > 0]
    average_profit = sum(list(company.values())[0] for company in profitable_companies) / len(profitable_companies)
    
    result = [dict(average_profit=average_profit), *companies]
    
    with open("company_data.json", "w") as json_file:
        json.dump(result, json_file)

def main_menu():
    while True:
        print("Меню:")
        print("1. Ввод данных в файл F1")
        print("2. Копирование строк без цифр из F1 в F2")
        print("3. Подсчет строк, начинающихся на 'А' в F2")
        print("4. Замена английских числительных на русские")
        print("5. Сформировать словарь с данными о предметах")
        print("6. Расчет прибыли компаний и сохранение в JSON")
        print("7. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            read_data_from_user()
        elif choice == '2':
            copy_lines_without_digits()
        elif choice == '3':
            count_lines_starting_with_A()
        elif choice == '4':
            replace_english_numbers_with_russian()
        elif choice == '5':
            subjects_dict = create_subjects_dict()
            print(subjects_dict)
        elif choice == '6':
            calculate_and_save_company_data()
        elif choice == '7':
            break
        else:
            print("Неверный выбор, попробуйте ещё раз.")

if __name__ == "__main__":
    main_menu()
