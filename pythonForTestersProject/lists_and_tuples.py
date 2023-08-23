empty_list = []
print(empty_list)

my_list = [1, 2, 3, "apple", 3.14]
print(my_list)
print(my_list[0])

sliced_list = my_list[1:4]
print(sliced_list)

my_list[3] = "banana"
print(my_list)

print(len(my_list))

my_list.append(10)
print(my_list)

my_list.extend([13, 'banana'])
print(my_list)

my_list.insert(0, 'zero')
print(my_list)

print(my_list.count("banana"))
print(my_list.index("banana"))

empty_tuple = ()
print(empty_tuple)

my_tuple = (1, 2, 3, "apple", 3.14)
print(my_tuple)

print(my_tuple[3])

print(my_tuple[1:4])

print(len(my_tuple))
print(my_tuple.count("apple"))
print(my_tuple.index("apple"))