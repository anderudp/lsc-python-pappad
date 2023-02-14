
# 1.feladat
# 10 első egész szám kinyomtatása
for i in range(5):
    print(i)
# Egyparaméteres range(): kódrész megismétlése valahány alkalommal

print()

# 2.feladat
# 10 első pozitív egész szám kinyomtatása
for i in range(1, 11):
    print(i)
# Kétparaméteres range(): mettől meddig haladjon a futóindex

print()

# 3.feladat
# Páros számok 2 és 100 között kinyomtatása
for i in range(2, 101, 2):
    print(i)
# Háromparaméteres range(): Ugyanaz, mint a kétparaméteres, csak változtatható lépésmértékkel

# 4.feladat
# Értékek generálása listába
my_list = []
# 20, 18, 16, 14, ... , -16, -18, -20
for j in range(20, -21, -2):
    my_list.append(j)
print(my_list)

# 5.feladat
# String lebontása betűkre
my_string = "Cicamancsa"
for letter in my_string:
    print(letter)

# 6.feladat
# Lista elemein végigmenni
names = ["Adél", "Béla", "Celcília", "Dénes", "Elemér", "Fyodr"]
for name in names:
    print(name)

print()

# 7.feladat
# Lista elemein végigmenni index alapján
# names = ["Adél", "Béla", "Celcília", "Dénes", "Elemér", "Fyodr"]
for i in range(len(names)):
    print(names[i])