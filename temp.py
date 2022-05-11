class Student:
    apitite = 'hungry'
    back_pack = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def add_courses(self, course_name):
   	    self.finished_courses =  [course_name]


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        student.grades[course] = [grade]

        
first_student = Student('Petya', 'Petrov', 'male')
second_student = Student('Alexey', 'Sherchenkov', 'male')


print(first_student.apitite)
print(second_student.apitite)
first_student.back_pack = 'zanachka'
first_student.apitite = 'poel'
print('#' * 10)
print(first_student.apitite)
print(first_student.back_pack)
print('#' * 10)
print(second_student.apitite)
print(second_student.back_pack)
third_student = Student('Ivan', 'Ivanov', 'male')
print('#' * 10)
print(third_student.apitite)
print(third_student.back_pack)
print('Objects_Dicty --> ')
print(first_student.__dict__)
print(second_student.__dict__)

print('Class_dict --> ')
print(Student.__dict__)