class Student:
    def __init__(self, name, age=None, grade=None):
        self.name = name
        self.age = age
        self.grade = grade

student1 = Student("Dmitry")
student2 = Student("Bom", 25)
student3 = Student("Charlie", grade="A")
student4 = Student("David", age=30, grade="B")