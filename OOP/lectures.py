class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __lt__(self, other):
        return self.count_avarage() < other.count_avarage()

    def __str__(self) -> str:
        return f"Имя: {self.name}\nФамилия: {self.surname}\nИзучаемые курсы:{self.courses_in_progress}\nСредняя оценка за домашние задания: {self.count_avarage()}"
    
    def count_avarage(self):
        if len(self.grades):
            return sum([sum(i) for i in self.grades.values()]) / sum([len(i) for i in self.grades.values()])
        else:
            return f"Нет курсов"

    def add_course(self, course_name):
        if course_name not in self.courses_in_progress:
            self.courses_in_progress += [course_name]

    def rate_lecturer(self, lecturer, course, grade):
            if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
                if course in lecturer.rates:
                    lecturer.rates[course] += [grade]
                else:
                    lecturer.rates[course] = [grade]
            else:
                return 'Ошибка'
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
    def course_attachement(self, course_name):
        self.courses_attached += [course_name]

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rates = {}

    def count_avarage(self):
        if len(self.rates):
            return sum([sum(i) for i in self.rates.values()]) / sum([len(i) for i in self.rates.values()])
        else:
            return f"Нет курсов"

    def __lt__(self, other):
        return self.count_avarage() < other.count_avarage()


    def __str__(self) -> str:
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.count_avarage()}"  

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    
    def rate_hw(self, student, course, grade):
            if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Ошибка'
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"
        
def get_students(students_list, courses_list):
    students = []
    for student in students_list:
        students.append(Student(student["name"], student["surname"], student["gender"]))

    for student in students:
        for course in courses_list:
            if student.name == course["name"]:
                student.courses_in_progress.extend(course["courses"])
    print(student.courses_in_progress)

    return students

students_list = [{"name": "Chipo", "surname": "Lino", "gender": "male"},
                 {"name": "Mal", "surname": "Vina", "gender": "female"}
                ]

courses_list = [{"name": "Chipo", "surname": "Lino", "courses": ["Math", "Chemistry", "Art"]},
                 {"name": "Mal", "surname": "Vina", "courses": ["Math", "Physics", "Music"]}
                ] 

student_1, student_2 = get_students(students_list, courses_list)

lecturer = Lecturer('Ivan', 'Ivanov')
lecturer.course_attachement('Math')

lecturer_2 = Lecturer('Lev', 'Landau')
lecturer_2.course_attachement('Physics')

student_1.add_course('Math')
student_1.add_course('Physics')
student_1.rate_lecturer(lecturer, 'Math', 7)
student_1.rate_lecturer(lecturer_2, 'Physics', 9)


rev = Reviewer('Ibragim', 'Rakhimov')
rev.course_attachement('Math')
rev.course_attachement('Physics')
rev.rate_hw(student_1, 'Math', 8)
rev.rate_hw(student_1, 'Physics', 7)


student_2.add_course('Math')
student_2.add_course('Physics')
student_2.rate_lecturer(lecturer, 'Math', 8)
student_2.rate_lecturer(lecturer_2, 'Physics', 10)

rev.rate_hw(student_2, 'Math', 9)
rev.rate_hw(student_2, 'Physics', 10)

print("Student 1: ", student_1, sep="\n")
print("Student 2: ", student_2, sep="\n")
print()
print("Lecturer: ", lecturer, sep="\n")
print("Lecturer 2: ", lecturer_2, sep="\n")
print()
print("Reviewer: ", rev, sep="\n")
