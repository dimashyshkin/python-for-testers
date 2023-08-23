a = 5  # Integer
x = -5
y = 1234567891011121212155484
print(a, x, y)

b = 3.14  # Float
d = -3.14
e = 3.0
print(b, d, e)

c = 2 + 3j  # Complex
print(c)

print(f"a is {type(a)}")
print(f"b is {type(b)}")
print(f"c is {type(c)}")
print(f"d is {type(d)}")
print(f"e is {type(e)}")
print(f"x is {type(x)}")
print(f"y is {type(y)}")

fl_a = float(a)
print(f"fl_a is {type(fl_a)}")

int_b = int(b)
print(f"int_b is {type(int_b)}")
print(a, b)
print(fl_a, int_b)