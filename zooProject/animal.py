class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def eat(self):
        print(f"{self._name} is eating")

    def sleep(self):
        print(f"{self._name} is sleeping")

    def make_sound(self):
        pass