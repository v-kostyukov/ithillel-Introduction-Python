class Student:
    grades = []

    def __init__(self, firstname, lastname, age, sex):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.sex = sex
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        avg_grade = 0
        count = 0
        if len(self.grades) > 1:
            for grade in self.grades:
                avg_grade += grade
                count += 1
            avg_grade = round(avg_grade / count, 2)
        elif len(self.grades) == 1:
            avg_grade = round(float(self.grades[0]), 2)

        return avg_grade


class Group:
    journal = []

    def __init__(self, group_name):
        self.group_name = group_name
        self.journal = []

    def add_student(self, student):
        self.journal.append(student)

    def remove_student(self, student):
        self.journal.remove(student)

    def print_journal(self):
        print(f"Журнал группы '{self.group_name}'", end='\n\n')
        if len(self.journal) > 0:
            for stud in self.journal:
                print('{:20s}{:^5d}{:^5s}'.format(' '.join([stud.firstname,
                                                            stud.lastname]),
                                                  stud.age, stud.sex), end='')
                if len(stud.grades) > 0:
                    for grade in stud.grades:
                        print('{:^3d}'.format(grade), end='')
                    print('{:^7.2f}'.format(stud.average()), end='\n')


student1 = Student('Petr', 'Ivanov', 20, 'M')
student2 = Student('Nikolay', 'Sidorov', 21, 'M')
group = Group('G-2021')

group.add_student(student1)
student1.add_grade(8)
student1.add_grade(10)
student1.add_grade(11)

group.add_student(student2)
student2.add_grade(10)
student2.add_grade(7)
student2.add_grade(8)

group.print_journal()
