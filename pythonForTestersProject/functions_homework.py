def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    return average

numbers = [10, 15, 20, 25, 30]

result = calculate_average(numbers)
print(f"The average of the numbers is {result}")