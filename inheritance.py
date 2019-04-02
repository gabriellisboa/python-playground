class Student:
    def __init__ (self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    
    def average(self):
        return sum(self.marks) / len(self.marks)

    def add_mark(self, mark):
        self.marks.append(mark)

    @classmethod
    def friend(cls, origin, friend_name, *args, **kwargs):
        return cls(friend_name, origin.school, *args, **kwargs)

class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        super().__init__(name, school)
        self.salary =  salary
        self.job_title = job_title

gabiroto = WorkingStudent("Gabiroto", "FMROOTS", 800, "Loja de calçados")
print(gabiroto.salary)

friend = gabiroto.friend(gabiroto, "Miguxo", 800, job_title='Loja de tintas')
print(friend.name)
print(friend.salary)
