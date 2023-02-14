current_date = input("Add meg a mai nap dátumát (ÉÉÉÉ-HH-NN): ")
born_date = input("Add meg a születési dátumod (ÉÉÉÉ-HH-NN): ")
days = 0
days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Dátum elválasztása évre, hónapra, napra
current_year, current_month, current_day = current_date.split('-')
born_year, born_month, born_day = born_date.split('-')

# Év, hónap, nap számmá alakítása
current_year, current_month, current_day = int(current_year), int(current_month), int(current_day)
born_year, born_month, born_day = int(born_year), int(born_month), int(born_day)

while not (born_year == current_year and born_month == current_month and born_day == current_day):
    # Szökőhónap
    if born_month == 2 and ((born_year % 4 == 0 and born_year % 100 != 0) or born_year % 400 == 0):
        if born_day < 29:
            born_day += 1
        else:
            born_month += 1
            born_day = 1
    else:
        if born_day < days_of_month[born_month - 1]:
            born_day += 1
        else:
            if born_month == 12:
                born_year += 1
                born_month = 1
                born_day = 1
            else:
                born_month += 1
                born_day = 1
    days += 1
print("Jelenleg %s nap az életkorod." % days)

# 2.feladat: Anagrammák

print()
word_1 = input("Add meg az első szót: ")
word_2 = input("Add meg a második szót: ")
if sorted(word_1.lower()) == sorted(word_2.lower()):
    print("A két szó anagramma.")
else:
    print("A két szó nem anagramma.")


# 3.feladat: Autók
speed = [96, 98, 72, 64, 93, 61]
slow_cars = 0
for i in range(len(speed) - 1):
    min_speed = speed[i + 1]
    for j in range(i + 1, len(speed) - 1):
        if speed[j] < min_speed:
            min_speed = speed[j]
    if speed[i] > min_speed:
        slow_cars += 1
print(slow_cars, "autónak kell lelassítania, hogy biztonságos legyen az út.")