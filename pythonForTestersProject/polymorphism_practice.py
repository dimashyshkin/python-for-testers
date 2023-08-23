class Vehicle:
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        print("The car drives on the road")


class Boat(Vehicle):
    def move(self):
        print("The boat sails on the water")


car = Car()
boat = Boat()

car.move()
boat.move()
