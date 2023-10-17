import os
import json


def main_menu():
    while True:
        print("Меню:")
        print("1. Ввод данных в файл F1")
        print("2. Копирование строк без цифр из F1 в F2")
        print("3. ")
        print("4. ")
        print("5. ")
        print("6. ")
        print("7. ")
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
