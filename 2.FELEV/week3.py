import math
import random
import matplotlib.pyplot as plt


def constants():
    print(math.pi)
    print(math.tau)
    print(math.e)
    print(math.inf)
    print(math.nan)


def circle(radius):
    print(f"T = {round(radius * math.tau, 3)} cm.")
    print(f"K = {round(radius ** 2 * math.pi, 3)} cm2.")


def operations():
    print(math.factorial(5))
    print(math.sqrt(4))
    print(math.fabs(-5))


def random_gen():
    numbers = []
    for i in range(100):
        numbers.append(random.randint(1, 10))
    print(numbers)


def game_time_distribution():
    n = int(input("Hány játékkal játszol?\n"))

    games = []  # játékok nevei
    game_times = []  # 1-10es játékidő
    game_time_pcts = []  # százalékos értékek

    time_sum = 0  # 1-10es értékek összege

    for i in range(n):
        games.append(input(f"Add meg a(z) {i+1}.játékot:\n"))
        time = int(input("Egy 1-10es skálán mennyi időt játszol vele?\n"))
        time_sum += time
        game_times.append(time)

    for time in game_times:
        pct = time / time_sum * 100
        pct = round(pct, 1)
        game_time_pcts.append(pct)

    plt.pie(game_time_pcts, labels=games, autopct='%.2f%%')
    plt.show()


def random_distribution():
    randoms = []
    for i in range(2000):
        randoms.append(random.randrange(0, 10, 2))

    names = ['Nulla', 'Kettő', 'Négy', 'Hat', 'Nyolc']
    counts = []

    for i in range(len(names)):
        counts.append(randoms.count(i * 2))

    plt.pie(counts, labels=names, autopct='%.0f%%')
    plt.show()

