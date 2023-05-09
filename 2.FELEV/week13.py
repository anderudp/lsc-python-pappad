import csv
import pandas as pd

# 1.feladat: Beolvasás csv modullal
def open_with_csv_module():
    csvfile = open("oscar_age_female.csv")
    data = csv.reader(csvfile, delimiter=" ")
    for row in data:
        print(' '.join(row))

# open_with_csv_module()

pd.set_option("display.width", 320)
pd.set_option("display.max_columns", 10)


# 2.feladat: Megnyitás Pandas-szal
def open_with_pandas():
    data = pd.read_csv("oscar_age_female.csv")
    print(data.head())

# open_with_pandas()


# 3.feladat: Átlag életkor
def average_oscar_winner_age():
    data = pd.read_csv("oscar_age_female.csv", usecols=["Age"])
    avg_age = data["Age"].mean()
    print(f"Az átlagos Oscar-díjas színésznő életkora: {round(avg_age, 2)} év.")


# average_oscar_winner_age()

# 4.feladat: Legfiatalabb, legöregebb
def youngest_oldest():
    data = pd.read_csv("oscar_age_female.csv", usecols=["Age", "Name"])
    min_age = data["Age"].min()
    min_row = data[data["Age"] == min_age]
    max_age = data["Age"].max()
    max_row = data[data["Age"] == max_age]
    print(f"A legfiatalabb díjnyertes {min_row.iloc[0, 1]}, {min_age} évesen.")
    print(f"A legöregebb díjnyertes {max_row.iloc[0, 1]}, {max_age} évesen.")

# youngest_oldest()


# 5.feladat: Fargo
def fargo_win():
    data = pd.read_csv("oscar_age_female.csv", usecols=["Year", "Movie"], skipinitialspace=True)
    fargo_row = data[data["Movie"] == "Fargo"]
    print(fargo_row)

# 6.feladat: Adatmegjelenítés
import matplotlib.pyplot as plt
def plot_ages_to_year():
    data = pd.read_csv("oscar_age_female.csv", usecols=["Age", "Year"])
    plt.scatter(data["Year"], data["Age"])
    plt.title("Életkor-évszám összefüggés")
    plt.show()

# plot_ages_to_year()

def plot_ages_pie():
    data = pd.read_csv("oscar_age_female.csv", usecols=["Age"])
    counts = data.value_counts()
    counts.plot(kind="pie")
    plt.title("Díjnyertesek életkor-eloszlása")
    plt.show()

plot_ages_pie()