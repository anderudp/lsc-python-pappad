my_tuple1 = ()
print(my_tuple1)
my_tuple2 = (1, 2, 3, 4)
print(my_tuple2)
my_tuple3 = (1, "hello", True, [0, 1, 3], my_tuple2)
print(my_tuple3)
my_tuple4 = ("hello",)
print(type(my_tuple4))

# Listák és tuple-ök
my_tuple5 = (1, 2, 3, 4)
print(type(my_tuple5))
my_tuple5 = list(my_tuple5)
print(type(my_tuple5))
my_tuple5 = tuple(my_tuple5)
print(type(my_tuple5))

my_tuple = (1, 2, 3)
my_list = [1, 2, 3]
my_list.append("hello")
del my_list[1]
print(my_list)

# Szeletelés
my_list = ["A", "B", "C"]
my_tuple = ("D", "E", "F")
print(my_list[:2], my_tuple[:2])
print(len(my_list), len(my_tuple))

import random
my_list = [random.randrange(0, 10) for i in range(100)]

random_color = tuple(random.randrange(0, 256) for i in range(3))
print(random_color)

my_tuple1 = (1, 2, 3, 9)
my_tuple2 = (4, 5, 6, 7)

print(my_tuple1 + my_tuple2)
print(my_tuple1 * 3)

# Feladat: my_tuple1 * 3 elemenként
multiple = []
for i in my_tuple1:
    multiple.append(i * 3)

my_multiplied_tuple = tuple(multiple)
print(my_multiplied_tuple)

my_multiplied_tuple_2 = tuple(element * 3 for element in my_tuple1)
print(my_multiplied_tuple_2)

# Tartalomellenőrzés
my_list = ["A", "B", "C", "D"]
my_tuple = (1, 2, 3, 4)
sanyi = ("Nemesi Sándor", 54, 178.6, True)
peti = ("Szarvasi Péter", 23, 205.0, False)
print("B" in my_list)
print(False in peti)

# List slicing kibővétes
my_list = ["A", "B", "C", "D", "E", "F"]
print(my_list[::-1])