

# 1.feladat
# Lista létrehozása
names = ["Antal", "Bálint", "Csenge", "Dénes", "Evelin"]
print(names)
print(type(names))

# 2.feladat
# Lista elemszáma/hossza
print("A lista hossza: " + str(len(names)))

# 3.feladat
# Konkrét elem lekérése
print(names[0])
element_2 = names[2]
print(element_2)

# 4.feladat
# Lista elemein végigmenni
i = 0
# ["Antal", "Bálint", "Csenge", "Dénes", "Evelin"]
while i < len(names):
    print(names[i])
    i += 1

# 5.feladat
# Elemek felvétele ciklussal
numbers = []
i = 1
while i <= 50:
    numbers.append(i)
    i += 1
print(numbers)

# 6.feladat
# Páros-páratlan lista
even_list = []
odd_list = []
i = 1
while i <= 100:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
    i += 1
print("Párosak: " + str(even_list))
print("Páratlanok: " + str(odd_list))