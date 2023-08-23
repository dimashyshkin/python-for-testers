empty_dict = {}
print(empty_dict)

my_dict = {"first_name": "Dmitry", "last_name": "Shyshkin", "age": 35}
print(my_dict)

print(f"{my_dict['first_name']} is {my_dict['age']} years old")

my_dict["language"] = "Python"
print(my_dict)

my_dict["language"] = "Java"
print(my_dict)

del my_dict["language"]
print(my_dict)

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())