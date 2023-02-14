

# 1.Feladat: Szöveg kinyomtatása több sorban
print("""Hello
World""")

# 2.Feladat: Megadott kúp térfogata
# radius = int(input("Add meg az alap kör sugarát:\n")) # radius = sugár
# height = int(input("Add meg a kúp magasságát:\n")) # height = magasság
# volume = (radius ** 2 * 3.14) * height / 3
# print("A kúp térfogata", volume, "egység.")

# 3.Feladat: 2 változó megcserélése
my_list = [0, 1, 3, 2]
print(my_list)

# Régi megoldás
temp = my_list[3]
my_list[3] = my_list[2]
my_list[2] = temp
print(my_list)

# Új megoldás
my_list = [0, 1, 3, 2]
print(my_list)
my_list[2], my_list[3] = my_list[3], my_list[2]
print(my_list)

# 4.Feladat: Számlista szétválasztása párosokra és páratlanokra
nums_list = [234, 11415, 12341, 345, 12, 754, 23, 53, 13467, 2]
evens = []  # párosak
odds = []  # páratlanok
for number in nums_list:
    if number % 2 == 0:
        evens.append(number)
    else:
        odds.append(number)
print("Művelet befejeződött.\nPárosak:", evens, "\nPáratlanok:", odds)

# 5.feladat: Legnépszerűbb gyümölcs
items = ["eper", "alma", "narancs", "körte", "licsi", "gránátalma"]
popularity = [12, 7, 16, 9, 3, 2]
max_popular = items[0]
for i in range(len(popularity) - 1):
    if popularity[i] < popularity[i+1]:
        max_popular = items[i+1]
print("A legnépszerűbb gyümölcs:", max_popular)

# 6.Feladat: Magánhangzók egy szövegben
text = "A mitokondrium a sejt erőműve."
print(text)
# magánhangzók
vowels = "aáeéiíoóöőuúüű"
vowel_count = 0
for char in text:
    if char in vowels:
        vowel_count += 1
print("A szövegben", vowel_count, "magánhangzó van.")

# 7.Feladat: N-faktoriális
n = int(input("Add meg a faktoriális számát:\n"))
factorial_product = 1
for i in range(1, n+1):
    factorial_product *= i
print(n, "faktoriális értéke:", factorial_product)