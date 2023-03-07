
import random

def create_matrix():
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [10, 11, 12]]
    print(matrix)


def create_matrix_2(row_count, column_count):
    matrix = []
    for i in range(row_count):
        row = []
        for j in range(column_count):
            row.append(0)
        matrix.append(row)
    print(matrix)

matrix2 = [["Never", "gonna", "give", "you", "up"],
              ["Never", "gonna", "let", "you", "down"],
              ["Never", "gonna", "run", "around", "and"],
              ["Desert", "you", "never", "gonna", "make"],
              ["You", "cry", "never", "gonna", "say"],
              ["Good", "bye", "never", "gonna", "tell"],
              ["A", "lie", "and", "hurt", "you"]]

def modify_matrix():

    print("Módosítás előtt:")
    for row in matrix2:
        print(row)

    mod_row = int(input("Add meg, melyik sorban akarsz változtatni:\n"))
    mod_col = int(input("Add meg, melyik oszlopban akarsz változtatni:\n"))
    change_to = input("Mire változtatnád az adott elemet:\n")

    matrix2[mod_row][mod_col] = change_to

    print("Módosítás után:")
    for row in matrix2:
        print(row)

def swimmers():
    data = ["cap number", "name", "age", "height", "weight"]
    team = [[1, "Michael", 37, 193, 90],
            [2, "Jolán", 2, 35, 5],
            [3, "János", 46, 190, 110],
            [8, "Juli", 32, 167, 46],
            [12, "Laci", 24, 218, 164]]

    print(team[2])
    print(team[-2])
    print(team[-1][3])
    print(team[1][-1])

    column = []
    for row in team:
        column.append(row[1])
    print(column)

def sorting_matrix():
    matrix = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(random.randrange(0, 256))
        matrix.append(row)

    print("Rendezés előtt:")
    for row in matrix:
        print(row)

    print("Rendezés után:")
    for i in range(len(matrix)):
        matrix[i] = sorted(matrix[i])

    for row in matrix:
        print(row)

sorting_matrix()