example_set = {1, 2, 3, 4, 5}

set_a = {1, 2, 3}
set_b = {3, 4, 5}
union = set_a.union(set_b)
print(union)

print(set_a.intersection(set_b))

difference = set_a.difference(set_b)
print(difference)

example_set.add(6)
print(example_set)
example_set.remove(1)
print(example_set)