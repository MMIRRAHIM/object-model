class Subject:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

class Student:
    def __init__(self, name):
        self.name = name
        self.subjects = {}

    def add_subject(self, subject):
        self.subjects[subject.name] = subject

    def add_grade(self, subject_name, grade):
        if subject_name in self.subjects:
            self.subjects[subject_name].add_grade(grade)

    def get_average(self):
        total = 0
        for subject in self.subjects.values():
            total += subject.get_average()
        return total / len(self.subjects) if self.subjects else 0

class Diary:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_average(self):
        total = 0
        for student in self.students:
            total += student.get_average()
        return total / len(self.students) if self.students else 0

math = Subject("Math")
physics = Subject("Physics")

arsen = Student("Arsen")

arsen.add_subject(math)
arsen.add_subject(physics)

arsen.add_grade("Math", 5)
arsen.add_grade("Physics", 4)

my_diary = Diary()

my_diary.add_student(arsen)

print(arsen.get_average())

print(my_diary.get_average())
