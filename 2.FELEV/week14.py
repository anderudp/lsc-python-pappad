import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option("display.width", 500)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

def letters():
    data = pd.read_csv("letter_frequency.csv")
    fig, ax = plt.subplots()
    ax.pie(data["Frequency"], labels=data["Letter"], autopct='%0.0f%%', pctdistance=0.9)
    plt.show()


def read_library():
    data = pd.read_csv("library.csv", usecols=["Identifier", "Title", "Author"])
    print(data.head(10))
    #print(data["Identifier"].is_unique)
    data = data.set_index("Identifier")
    print(data.head(10))
    data = data.drop(columns=["Author"])
    print(data.head(10))


def book_by_id(row_id):
    data = pd.read_csv("library.csv").set_index("Identifier")
    print(data.loc[row_id])


book_by_id(7521)