class Parent:
    def __init__(self):
        print("Parent class is created")

    def speak(self):
        print("Parent is speaking")


class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child class is created")

    def speak(self):
        super().speak()
        print("Child is speaking")

child = Child()
child.speak()