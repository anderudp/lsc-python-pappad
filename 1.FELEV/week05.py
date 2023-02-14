
"""
num_1 = 1
while True:
    print(num_1)
    num_1 += 1
"""

# 1.feladat
num_2 = 1
summ = 0
while num_2 <= 10:
    print(num_2)
    summ += num_2
    num_2 += 1
print(summ)

# 2.feladat
num_3 = 24562728258851
count = 0
while num_3 != 0:
    print(num_3)
    num_3 //= 10
    count += 1
print("Számjegyek száma " + str(count))

# 3.feladat
solution = 42
remaining_guesses = 7
guess = 0
while guess != solution and remaining_guesses > 0:
    guess = int(input("Add meg a tippedet 1 és 100 között:\n"))
    if guess > solution:
        print("Kisebb számra gondoltam.")
    elif guess < solution:
        print("Nagyobb számra gondoltam.")
    remaining_guesses -= 1
    print("Hátralévő tippek száma: " + str(remaining_guesses))
if guess == solution:
    print("Gratulálok, sikeres tipp volt!")
else:
    print("Sajnos vesztettél.")