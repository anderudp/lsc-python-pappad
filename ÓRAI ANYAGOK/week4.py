
# 1.feladat
# Számtani operátorok

# Összeadás
print(5 + 5)

# Kivonás
print(5 - 3)

# Szorzás
print(2 * 7)

# Osztás
print(9 / 3)
print(10 / 3)

# Hatványozás
print(2 ** 3)

# Osztás alsó egészrésze
print(99 / 4)
print(99 // 4)

# Osztás maradéka / moduló
print(99 / 4)
print(99 % 4)
print(99 % 2)

# 2.feladat
# Értékadó operátorok

num = 8
print(num)
num += 7
print(num)
num -= 6
print(num)
num *= 5
print(num)
num /= 3
print(num)
num **= 2
print(num)
num //= 2
print(num)
num %= 3
print(num)

# 3. feladat
# Összehasonlító operátorok
print(5 > 4)
print(9 * 5 == 45)

# 4. feladat
# Tartalmi operátor
char_1 = "H"
char_2 = "x"
text = "Hello"
print(char_2 in text)

# 5. feladat
can_fly = input("Tud-e repülni az állat? (igen/nem)")
can_swim = input("Tud-e úszni az állat? (igen/nem)")
legs_count = int(input("Hány lába van az állatnak? (4/2)"))
if can_fly == "igen":
    if can_swim == "igen":
        if legs_count == 2:
            print("A hattyúra gondoltál!")
        elif legs_count == 4:
            print("Az unikornisra gondoltál!")
    elif can_swim == "nem":
        if legs_count == 2:
            print("Galambra gondoltál!")
        elif legs_count == 4:
            print("A szúnyogra gondoltál!")