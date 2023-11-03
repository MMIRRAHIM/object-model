class Subject:
    def __init__(self, name):
        self._name = name
        self._grades = []

    def add_grade(self, grade):
        if 1 <= grade <= 5:
            self._grades.append(grade)
        else:
            raise ValueError("Grade must be between 1 and 5.")

    def get_average_grade(self):
        return sum(self._grades) / len(self._grades) if self._grades else 0

    @property
    def name(self):
        return self._name

    @property
    def grades(self):
        return self._grades[:]


class Student:
    def __init__(self, name):
        self._name = name
        self._subjects = {}

    def add_subject(self, subject):
        if subject.name not in self._subjects:
            self._subjects[subject.name] = subject
        else:
            raise ValueError(f"Subject {subject.name} already exists.")

    def add_grade(self, subject_name, grade):
        if subject_name in self._subjects:
            self._subjects[subject_name].add_grade(grade)
        else:
            raise ValueError(f"Subject {subject_name} is not registered for this student.")

    def get_average_grade(self):
        total = sum(subject.get_average_grade() for subject in self._subjects.values())
        return total / len(self._subjects) if self._subjects else 0

    @property
    def name(self):
        return self._name

    @property
    def subjects(self):
        return self._subjects.copy()


class Diary:
    def __init__(self):
        self._students = []

    def add_student(self, student):
        if student not in self._students:
            self._students.append(student)
        else:
            raise ValueError("Student already exists in the diary.")

    def get_student_average(self, student_name):
        student = next((s for s in self._students if s.name == student_name), None)
        if student is not None:
            return student.get_average_grade()
        else:
            raise ValueError(f"Student {student_name} not found in the diary.")

    @property
    def students(self):
        return self._students[:]

math = Subject("Mathematics")
physics = Subject("Physics")

arsen = Student("Arsen")

arsen.add_subject(math)
arsen.add_subject(physics)

arsen.add_grade("Mathematics", 4)
arsen.add_grade("Mathematics", 5)
arsen.add_grade("Physics", 3)

print(f"Arsen's average in Mathematics: {arsen.get_average_grade()}")

school_diary = Diary()

school_diary.add_student(arsen)

print(f"Arsen's average in diary: {school_diary.get_student_average('Arsen')}")

