class Car:
    wheels = 4

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self, miles):
        print(f"{self.make} {self.model} drove for {miles} miles")

    @classmethod
    def set_wheels(cls, num_wheels):
        cls.wheels = num_wheels

    @staticmethod
    def miles_to_kilometers(miles):
        return miles * 1.6