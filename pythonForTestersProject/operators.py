x = 5
print(x)

y = x + 3
print(y)

z = y / 2
print(z)

x += 3
print(x)

x /= 2
print(x)

print("- - - - - - - - - ")

print(x == y)
print(x != y)
print(x > y)
print(x <= y)

print("- - - - - - - - - ")

fruits = ['apple', 'banana', "cherry"]
print("banana" in fruits)
print('mango' not in fruits)

print("- - - - - - - - - ")

a = 5
b = 5
print(a is b)
print(a == b)

list_a = [1, 3, 5]
list_b = [1, 3, 5]
print(list_a is list_b)
print(list_a == list_b)

print("=====")
list_c = list_a
print(list_c is list_a)

list_d = list_a.copy()
print(list_d is list_a)
print(list_d == list_a)