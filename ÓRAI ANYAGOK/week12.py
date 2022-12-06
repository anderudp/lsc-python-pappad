
"""
user_numbers = []
for i in range(10):
    new_number = int(input("Adj meg egy számot:\n"))
    user_numbers.append(new_number)
odd = 0  # páratlan
even = 0  # páros
positive = 0
negative = 0
zero = 0
for num in user_numbers:
    if num > 0:
        positive += 1
    elif num == 0:
        zero += 1
    else:
        negative += 1
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Páros számok:", even, "\nPáratlan számok:", odd, "\nPozitív számok:", positive,
      "\nNegatív számok:", negative, "\nNullák:", zero)
"""

# 2.feladat: Gyűjtemények összeolvasztása
my_list = [1, 2, 3, 4, 5]
print(my_list)
my_list.extend([6, 7, 8])
print(my_list)

# 3.feladat: véletlen számok elemzéze
rnd_nums = [805, 931, 395, 141, 360, 100, 459, 282, 373,  36, 977, 212, 964, 905, 635, 409, 798, 590,  69, 361, 959,  17, 390, 421, 751, 588, 429, 233, 162, 325,  39, 295, 674, 304, 957,  57, 441, 137, 112, 129, 727, 645, 593, 984, 910, 426, 498, 392,  18, 584,  25, 693]
smallest = min(rnd_nums)
print("A legkisebb szám:", smallest)
greatest = max(rnd_nums)
print("A legnagyobb szám:", greatest)
print("A legkisebb szám indexe:", rnd_nums.index(smallest))
print("A legnagyobb szám indexe:", rnd_nums.index(greatest))

# 4.feladat: lista rendezése
bubble_list = rnd_nums[:]
i = len(bubble_list) - 1
while i > 0:
    for j in range(i):
        if bubble_list[j] > bubble_list[j+1]:
            temp = bubble_list[j]
            bubble_list[j] = bubble_list[j+1]
            bubble_list[j+1] = temp
    i -= 1
print(bubble_list)

# 5.feladat: sorted()
print(sorted(rnd_nums))