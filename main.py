class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.sredocenka = 0

    def rate_hw_lectoue(self, lectour, course, grade):
        if isinstance(lectour,
           Lecturer) and course in lectour.courses_attachedlect:
            if course in lectour.gradeslect:
                    lectour.gradeslect[course] += [grade]
            else:
                    lectour.gradeslect[course] = [grade]
        else:
            return 'Ошибка'
    def sredocenkstud(self):
        dl = 0
        sumoc = 0
        dl2 = 0
        for value in self.grades.values():

            dl2 = len(value)
            maxdl = 0
            while maxdl < dl2:
                dl += 1
                sumoc += value[maxdl]
                maxdl += 1
        res = round(sumoc / dl, 2)
        return res
    def __lt__(self, other):
        return self.sredocenkstud() < other.sredocenkstud()
    def __str__(self):
        prcourses = ''
        dl = 0
        for value in self.courses_in_progress:
            if dl>0:
                prcourses += ', '
            prcourses += value
            dl +=1
        dl = 0
        prendcourses = ''
        for value in self.finished_courses:
            if dl>0:
                prendcourses += ', '
            prendcourses += value
            dl +=1
        self.sredocenka = self.sredocenkstud()
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.sredocenka}\nКурсы в процессе изучения:{prcourses}\nЗавершенные курсы:{prendcourses}'
        return res




class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []





#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)

# print(best_student.grades)

class Lecturer (Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_in_progresslect = []
        self.courses_attachedlect = []
        self.gradeslect = {}

    def __lt__(self, other):
        return self.sredocenklector() < other.sredocenklector()
    def sredocenklector(self):
        dl = 0
        sumoc = 0
        dl2 = 0
        for value in self.gradeslect.values():

            dl2 = len(value)
            maxdl = 0
            while maxdl < dl2:
                dl += 1
                sumoc += value[maxdl]
                maxdl += 1
        srznach = round(sumoc / dl, 2)
        return srznach
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.sredocenklector()}'
        return res

class Reviewer (Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

def sredochomework (student, name_kurs):
    pass








best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Delphi']
best_student.finished_courses += ['C#']

best_student2 = Student('Roman', 'Gulaev', 'your_gender')
best_student2.courses_in_progress += ['Python']

roman = Reviewer('Roman', 'Petrov')
roman.courses_attached += ['Python']
roman.rate_hw(best_student, 'Python', 10)
roman.rate_hw(best_student2, 'Python', 4)
print(best_student.grades)



lect1 = Lecturer('Ivan', 'Ivanov')
lect1.courses_attachedlect += ['Delphi']
lect1.courses_attachedlect += ['C#']
lect2 = Lecturer('Ivan2', 'Ivanov2')
lect2.courses_attachedlect += ['Delphi']
best_student.rate_hw_lectoue(lect2, 'Delphi', 7)

best_student.rate_hw_lectoue(lect1, 'Delphi', 10)
best_student.rate_hw_lectoue(lect1, 'Delphi', 8)
best_student.rate_hw_lectoue(lect1, 'C#', 7)
# student_petrov = Student('Serg', 'Petrov', 'your_gender')
# student_petrov.rate_hw_lectoue(lect1, 'Delphi', 10)


print(lect1.courses_attachedlect)
print(lect1.gradeslect)


rev1 = Reviewer('Petr', 'Kuchin')
print(rev1)
print(lect1)
print(best_student)
print (best_student < best_student2)
print (lect1 > lect2)