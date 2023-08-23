n = 25

sum_of_all_numbers = 0

for i in range(n):
    if i % 3 == 0 or i % 5 == 0:
        sum_of_all_numbers += i

print(f"Sum of multiples of 3 and 5 up to {n} is: {sum_of_all_numbers}")

sum_of_all_numbers_while_loop = 0
current_number = 1
while current_number < n:
    if current_number % 3 == 0 or current_number % 5 == 0:
        sum_of_all_numbers_while_loop += current_number
    current_number += 1
print(f"Sum of multiples of 3 and 5 up to {n} is: {sum_of_all_numbers_while_loop}")
