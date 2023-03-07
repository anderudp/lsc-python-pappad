
import random
import matplotlib.pyplot as plt
import numpy as np

# 1.feladat: Négyzetszámok
def next_square():
    k = 1
    while True:
        yield k**2
        k += 1


# for square in next_square():
#     if square > 100:
#         break
#     print(square)

# 2.feladat
def next_even(values):
    for item in values:
        if item % 2 == 0:
            yield item

# test_list = []
# while len(test_list) < 20:
#     rand = random.randrange(1, 100)
#     if rand not in test_list:
#         test_list.append(rand)
#
# print(f"Az eredeti listánk: {test_list}")
# print("A listánk páros számai: ", end=" ")
# for even in next_even(test_list):
#     print(even, end=", ")

# 3.feladat: Kő-papír-olló
options = ["Kő", "Papír", "Olló"]
def RPS():
    winner = 0  # 0 - döntetlen, 1 - játékos nyer, 2 - gép nyer
    rand = random.randint(0, 2)
    computer_input = options[rand]
    computer_input = computer_input.lower()
    print(f"A számítógép {computer_input}-t dobott.")
    if user_input == computer_input:
        winner = 0
    elif (user_input == options[0].lower() and computer_input == options[2].lower()) or (user_input == options[1].lower() and computer_input == options[0].lower()) or (user_input == options[2].lower() and computer_input == options[1].lower()):
        winner = 1
    else:
        winner = 2
    return winner

win = lose = tie = 0
round_count = int(input("Hány kört akarsz játszani?\n"))
for i in range(round_count):
    print(f"{i + 1}.kör")
    user_input = input(f"Válassz az alábbiak közül: {options}")
    user_input = user_input.lower()
    game = RPS()
    if game == 0:
        print("Döntetlen.")
        tie += 1
    elif game == 1:
        print("Te nyertél!")
        win += 1
    else:
        print("A gép nyert.")
        lose += 1

print(f"Győztes körök: {win}\nVesztes körök: {lose}\nDöntetlenek: {tie}")


def chart():
    fig, ax = plt.subplots()
    labels = ["Győzelmek", "Vesztések", "Döntetlenek"]
    y_pos = np.arange(len(labels))

    ax.barh(y_pos, [win, lose, tie], align="center")
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels)
    ax.set_title("Játék eredmények")
    ax.set_xlabel("Teljesítmény")
    ax.invert_yaxis()
    plt.show()

chart()