class Student:
    def __init__(self, name: str, marks: int):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        return self.marks > 50


stud1 = Student("Jan", 76)
stud2 = Student("Adam", 32)

print(stud1.is_passed())
print(stud2.is_passed())
