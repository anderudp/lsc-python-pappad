
SOLUTION = "a mitokondrium a sejt erőműve"
PUZZLE_STATE = "_ ____________ _ ____ _______"
LIFE = 10
CORRECT_LETTERS = []
INCORRECT_LETTERS = []

while LIFE > 0 and PUZZLE_STATE != SOLUTION:
    print(PUZZLE_STATE)
    guess = input("Tippelj egy betűt, vagy megoldást:\n")
    if len(guess) == 1:
        found_something = False
        state_list = list(PUZZLE_STATE)
        for i in range(len(SOLUTION)):
            if SOLUTION[i] == guess:
                state_list[i] = guess
                found_something = True
        PUZZLE_STATE = ''.join(state_list)
        if found_something:
            print("Talált a betű. Életek száma: " + str(LIFE))
            CORRECT_LETTERS.append(guess)
        else:
            LIFE -= 1
            print("Ez a betű nincs benne a megoldásban. Életek száma: " + str(LIFE))
            INCORRECT_LETTERS.append(guess)
    else:
        if guess == SOLUTION:
            print("Eltaláltad a megoldást!!")
            PUZZLE_STATE = guess
        else:
            LIFE -= 1
            print("A megoldásod helytelen. Életek száma: " + str(LIFE))
    print("Helyes betűk: " + ", ".join(CORRECT_LETTERS))
    print("Téves betűk: " + ", ".join(INCORRECT_LETTERS))
    print()
if LIFE > 0:
    print("Szép munka!")
else:
    print("Ez most nem jött össze.")

# 2.feladat
# Kvadránsok ábra: https://www.math.net/img/a/geometry/coordinate-plane/quadrant/signs-of-quadrant.png
num_x = int(input("Add meg az x-koordinátát:\n"))
num_y = int(input("Add meg az y-koordinátát:\n"))

if num_x > 0:
    if num_y > 0:
        print("I.kvadráns")  # x pozitív, y pozitív
    elif num_y < 0:
        print("IV.kvadráns")  # x pozitív, y negatív
    else:
        print("Az x-tengely jobb oldala")  # x pozitív, y nulla
elif num_x < 0:
    if num_y > 0:
        print("II.kvadráns")  # x negatív, y pozitív
    elif num_y < 0:
        print("III.kvadráns")  # x negatív, y negatív
    else:
        print("Az x-tengely bal oldala")  # x negatív, y nulla
else:
    if num_y > 0:
        print("Az y-tengely felső oldala")  # x nulla, y pozitív
    elif num_y < 0:
        print("Az y-tengely alsó oldala")  # x nulla, y negatív
    else:
        print("Origó")  # x nulla, y nulla