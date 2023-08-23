from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, make: str, model: str, year: int, cargo_capacity: int):
        super().__init__(make, model, year)
        self.__cargo_capacity = cargo_capacity

    def load_cargo(self, weight: int):
        if weight > self.__cargo_capacity:
            return f"Cargo exceeds {self.year} {self.make} {self.model} capacity!"
        return f"Cargo of {weight} kg loaded succesfully!"