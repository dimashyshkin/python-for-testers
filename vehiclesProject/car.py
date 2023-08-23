from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int, is_electric: bool):
        super().__init__(make, model, year)
        self.is_electric = is_electric

    def start_engine(self):
        if self.is_electric:
            return f"The {self.year} {self.make} {self.model} starts silently"
        else:
            return super().start_engine()