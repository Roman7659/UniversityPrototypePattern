import copy

class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def clone(self):
        return copy.deepcopy(self)

# Створення студента
original_student = Student("John Doe", 20, "Computer Science")

# Клонування студента
cloned_student = original_student.clone()

# Зміна деяких характеристик клонованого студента
cloned_student.name = "Jane Smith"
cloned_student.age = 21

print(original_student.name, original_student.age, original_student.major)  # Виведе: John Doe 20 Computer Science
print(cloned_student.name, cloned_student.age, cloned_student.major)  # Виведе: Jane Smith 21 Computer Science
 
