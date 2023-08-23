from car import Car
from truck import Truck

my_car = Car("Tesla", "Model Y", 2023, True)
print(my_car.start_engine())

my_classic_car = Car("Ford", "Mustang", 1965, False)
print(my_classic_car.start_engine())

my_truck = Truck(make="Ford", model="F-150", year=2020, cargo_capacity=1000)
print(my_truck.start_engine())
print(my_truck.load_cargo(500))