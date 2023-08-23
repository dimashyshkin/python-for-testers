import math
import random
import statistics

root = math.sqrt(16)
print(root)

print(math.pi)
print(math.e)

print(round(5.4))
print(math.floor(5.4))
print(math.ceil(5.4))

print("- - - - - - - -- - - - - - - -")
rand_int = random.randint(90, 100)
print(rand_int)

rand_range = random.randrange(1, 10)
print(rand_range)

rand_float = random.random()
print(rand_float)

rand_choice = random.choice([1, 2, 3, 4, 5])
print(rand_choice)

list = [1, 2, 3, 4, 5]
random.shuffle(list)
print(list)

print("------------------------------")
data = [2, 3, 4, 5, 7, 9, 2, 4, 6, 8, 10, 15]

data_mean = statistics.mean(data)
print(f"The mean of data set is {data_mean}")

data_median = statistics.median(data)
print(f"The median of data set is {data_median}")

data_mode = statistics.mode(data)
print(f"The mode of data set is {data_mode}")

data_stdev = statistics.stdev(data)
print(f"The stdev of data set is {data_stdev}")