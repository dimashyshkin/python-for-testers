def hello_world():
    print("Hello, World!")


hello_world()


def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")


greet("Dmitry", 35)


def sum_numbers(*numbers):
    total = 0
    for number in numbers:
        total += number
    print(total)


sum_numbers(2, 3, 4)
sum_numbers(1, 2, 3, 4, 5)


def display_info(name, age, city="Unknown"):
    print(f"Name: {name}, age: {age}, city: {city}")


display_info("Alice", 30)
display_info(name="Bob", age=40, city="New York")


def display_fruits(fruits_list):
    for fruit in fruits_list:
        print(fruit)


my_fruits = ["Apple", "Banana", "Cherry"]
display_fruits(my_fruits)

def multiply(a, b):
    result = a * b
    return result

result = multiply(5, 4)
print(result)

def calculate(a, b):
    sum = a + b
    diff = a - b
    return sum, diff

result_sum, result_diff = calculate(7, 3)
print(f"Sum: {result_sum}, Diff: {result_diff}")