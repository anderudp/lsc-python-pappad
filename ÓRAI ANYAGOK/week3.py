

pet_name = "Pufi"
pet_species = "hörcsög"
pet_age = 0.01
pet_weight = 0.2

print("A nevem " + pet_name + ", a " + pet_species + ", az életkorom " + str(pet_age) + ", a testsúlyom " + str(pet_weight))

# 1.feladat
# Százalékjeles behelyettesítés
print("A nevem %s, a %s, az életkorom %s, a testsúlyom %s" %(pet_name, pet_species, pet_age, pet_weight))

# 2.feladat
# Elágazások
if pet_species == "hörcsög":
    if pet_weight >= 0.2:
        print("Kövér a hörcsögöd!!")
    elif pet_weight <= 0.08:
        print("Eteted te egyáltalán a hörcsögöd?!")
    else:
        print("Pacek a hörcsögöd :)")
    if pet_age > 3:
        print("Micsoda matuzsálemi példány!")
    elif pet_age < 0.15:
        print("Bébihörcsög <3")
    else:
        print("Sztenderd hörcsög.")

# 3.feladat
# Osztályzás
points = int(input("Írtál egy 100 max pontszámú dolgozatot. Hány pontot értél el?"))
if points >= 90:
    print("Ötöst kaptál! :D")
elif points >= 75:
    print("Négyes lett! :)")
elif points >= 60:
    print("Hármas. :|")
elif points >= 50:
    print("Kettes -.-")
else:
    print("Megbuktál D:")