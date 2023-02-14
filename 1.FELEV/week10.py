# 1.feladat - Listaelemek kinyomtatása for ciklussal külön sorokba
myList = []
for i in range(5):
    myList.append(i)
for element in myList:
    print(element)

# 2.feladat - Listaelemek kinyomtatása for ciklussal egy sorba
for element in myList:
    print(element, end=", ")

print()

# 3.feladat - Többparaméteres print
first = "mitokondrium"  # kiscica - kávé
second = "sejt"  # szív - agy
print("A", first, "a", second, "erőműve.")

# 3.feladat - Elválasztó karakter felülírása többparaméteres print()-ben
year = input("Please enter the year\n")
month = input("Please enter the month\n")
day = input("Please enter the day\n")
print(month, day, year, sep="/")

# 4.feladat - Konvertáló
types = input("Please enter the type of converter: (dist, temp)\n")
# Celsius(c)-Fahrenheit(f) converter
if types == "temp":
    x = float(input("The value: "))
    unit = input("The unit: ")
    if unit == "c":
        print(str(x) + " Celsius in Fahrenheit: " + str((x*1.8)+32))
    elif unit == "f":
        print(str(x) + " Fahrenheit in Celsius: " + str((x-32)/1.8))
    else:
        print("Not a real unit!")
# km-miles(m) converter
elif types == "dist":
    x = float(input("The value: "))
    unit = input("The unit: ")
    if unit == "km":
        print(str(x) + " km in miles: " + str(x*0.62137))
    elif unit == "m":
        print(str(x) + " miles in km: " + str(x/0.62137))
    else:
        print("Not a real unit!")
else:
    print("No such converter found!")


# Task 8 - Triangle types
myList = []
a = float(input("Első oldal: "))
b = float(input("Második oldal: "))
c = float(input("Harmadik oldal: "))
if a + b > c and a + c > b and b + c > a:  # Háromszög-egyenlőtlenség tétele
    print("A háromszög létezik.")
if a == b == c:
    print("Szabályos/Egyenlő oldalú háromszög.")  # Regular/Equilateral triangle
elif a == b or b == c or a == c:
    print("Egyenlő szárú háromszög.")  # Isosceles triangle
elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:  # Pitagorasz-tétel
    print("Derékszögű háromszög.")  # Right triangle
else:
    print("Egyszerű háromszög.")
