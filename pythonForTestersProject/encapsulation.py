class Encapsulation:
    def __init__(self):
        self.public = "I'm public"
        self._protected = "I'm protected"
        self.__private = "I'm private"

    @property
    def private(self):
        return self.__private

    @private.setter
    def private(self, value):
        self.__private = value


encapsulated_object = Encapsulation()
print(encapsulated_object.public)
print(encapsulated_object._protected)
encapsulated_object.private = "I've been changed"
print(encapsulated_object.private)