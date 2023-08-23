from car import Car
from driver import Driver


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


my_cat = Cat("Whiskers", 3)

my_car = Car("Toyota", "Camry", 2014)
me = Driver("Dmitry", 35)
print(f"{me.age} years old {me.name} is driving {my_car.make} {my_car.model} {my_car.year}")

friends_car = Car("Toyota", "Rav4", 2020)
friend = Driver("Olga", 35)
print(f"My {friend.age} years old friend {friend.name} is driving {friends_car.make} {friends_car.model} {friends_car.year}")

print(f"My car has {my_car.wheels} wheels")
print(f"My friends car has {friends_car.wheels} wheels")


my_car.year = 2015
Car.wheels = 6

print(my_car.year)
print(friends_car.year)
print(my_car.wheels)
print(friends_car.wheels)

my_car.drive(100)
friends_car.drive(50)

Car.set_wheels(8)
print(my_car.wheels)
print(friends_car.wheels)

kilometers = Car.miles_to_kilometers(100)
print(kilometers)

kilometers_2 = my_car.miles_to_kilometers(100)
print(kilometers_2)
