customers_age = 45
time_of_the_day = 1600

base_price = 12.0

if customers_age <= 12:
    discount = 0.5
elif customers_age >= 60:
    discount = 0.3
elif time_of_the_day < 1700:
    discount = 0.2
else:
    discount = 0

final_price = base_price * (1-discount)
print(f"The final ticket price is ${final_price:.2f}")