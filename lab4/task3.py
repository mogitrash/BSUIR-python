class Faculty:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_students(self):
        return self.students

class Student:
    def __init__(self, full_name, birth_year):
        self.full_name = full_name
        self.birth_year = birth_year
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_grades(self):
        return self.grades

    def get_average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

# Пример использования:
faculty = Faculty("Информатика и вычислительная техника")

student1 = Student("Иванов Иван Иванович", 2000)
student1.add_grade(85)
student1.add_grade(92)
student1.add_grade(78)

student2 = Student("Петров Петр Петрович", 1999)
student2.add_grade(70)
student2.add_grade(65)
student2.add_grade(88)

faculty.add_student(student1)
faculty.add_student(student2)

students = faculty.get_students()
for student in students:
    print(f"Студент: {student.full_name}")
    print(f"Год рождения: {student.birth_year}")
    print(f"Оценки: {student.get_grades()}")
    print(f"Средний балл: {student.get_average_grade()}")
    print()

# Результат:
# Студент: Иванов Иван Иванович
# Год рождения: 2000
# Оценки: [85, 92, 78]
# Средний балл: 85.0
#
# Студент: Петров Петр Петрович
# Год рождения: 1999
# Оценки: [70, 65, 88]
# Средний балл: 74.33333333333333
