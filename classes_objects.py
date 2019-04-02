class LoterryPlayer:
    def __init__(self, name, numbers):
        self.name = name
        self.numbers = numbers

    def total(self):
        return sum(self.numbers)


player = LoterryPlayer('gabiroto', (11, 24, 69))

print(player.name)
print(player.numbers)
print(player.total())


class Student:
    def __init__(self, name, school, marks):
        self.name = name
        self.school = school
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    @staticmethod
    def go_to_school():
        print("I'm going to School")

    @classmethod
    def go_home(cls):
        print("I'm going Home")

    def go_to_gym(self):
        print("I'm going to the gym")

anna = Student("Anna", "MIT", (11, 69, 24))
anna.go_to_school()
Student.go_home()
anna.go_to_gym()