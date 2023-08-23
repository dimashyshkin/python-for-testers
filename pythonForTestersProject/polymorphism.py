class Parent:
    def greet(self, name=None):
        if name is None:
            return "Hello, unknown person."
        else:
            return f"Hello, {name}"

class Child(Parent):
    def greet(self, name=None):
        if name is None:
            return "Hey, who are you?"
        else:
            return f"Hey, {name}"



parent = Parent()
print(parent.greet())
print(parent.greet("Dmitry"))

child = Child()
print(child.greet())
print(child.greet("Roman"))