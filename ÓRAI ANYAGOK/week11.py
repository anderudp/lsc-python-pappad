

# 1.feladat - egész számok 1-től 9-ig derékszögű háromszög alakban
for i in range(1, 10):
    for j in range(i):
        print(i, end=" ")
    print()

# 2.feladat - 7 és 4 többszörösei 1300 és 2100 között
for i in range(1300, 2101):
    if i % 7 == 0 and i % 4 == 0:
        print(i, end=", ")
print()
for i in range(1300, 2101):
    if i % 28 == 0:
        print(i, end=", ")

# 3.feladat - névkombinációk
family_names = ["Lakatos", "Molnár", "Ács", "Kovács", "Szabó"]
given_names = ["Bálint", "Rikárdó", "Attila", "Brendon", "Levente"]
for fname in family_names:
    for gname in given_names:
        print(fname, gname)

# 4.feladat - prím-e a számunk
my_number = ""
while not my_number.isdecimal():
    my_number = input("Adj meg egy számot, amire ellenőrizzük, hogy prím-e!\n")

my_number = int(my_number)

prime_divisors = []
for i in range(1, my_number+1):
    if my_number % i == 0:
        prime_divisors.append(i)

if len(prime_divisors) > 2:
    print(my_number, "nem prímszám, mert van", len(prime_divisors), "osztója.")
elif len(prime_divisors) == 2:
    print(my_number, "prímszám.")
else:
    print("Az 1 definíció szerint nem prímszám.")

# 5.feladat - Collatz-sejtés
number = int(input("Add meg a sorozat kezdőértékét"))
collatz = [number]
while number != 1:
    if number % 2 == 0:
        number /= 2
        number = int(number)
        collatz.append(number)
    else:
        number = 3 * number + 1
        number = int(number)
        collatz.append(number)
print(collatz)