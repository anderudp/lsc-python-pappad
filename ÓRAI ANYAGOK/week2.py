
# 1.feladat
# Szöveg hossza
text = "A mitokondrium a sejt erőműve"
print("A szöveg hossza:" + str(len(text)))

# 2.feladat
# Szöveg elválasztása
text = "A mitokondrium a sejt erőműve"
split_text = text.split(' ')
print(split_text)

# 3.feladat
# Szövegrész számlálása
text = """Keljetek fel, gyertek velem!
E percben kell cselekednem!
Rekesszenek be esetleg?
Ez kell nektek?! Feleljetek!
Nemzetem szent fejedelme,
Megteszem,
Megteszem: e nemes tettet
Szervezem!"""
print("E betűk száma: " + str(text.count('e') + text.count('E')))

# 4.feladat
# Keresés szövegen belül
text = "A mitokondrium a sejt erőműve"
print("A \"sejt\" szó a " + str(text.find("sejt")) + " indexen fordul elő.")  # \ jelhez: AltGr + Q

# 5.feladat
# Szöveg tartalma
text = input("Adj meg egy számot:")
print("Valóban számot adtál meg: " + str(text.isdecimal())) # isnumeric() is létezik
text = "Hello world"
print("A szövegünk kisbetűs: " + str(text.islower()))  # isupper() is létezik
text = "Kisjani"
print("Csak betűket tartalmaz a szöveg: " + str(text.isalpha()))

# 6.feladat
# Hozzunk létre egy embert
person_name = "Gipsz Jakab"
person_hair_color = "Barna"
person_birth_year = 2001
person_weight = 77.6

print("A nevem " + person_name + ", a hajam színe " + person_hair_color + ", " + str(person_birth_year)
      + "-ben születtem, a testsúlyom " + str(person_weight) + "kg.")
