
import random
import matplotlib.pyplot as plt
import numpy

def tax_calculator(income):
    if income < 9875:
        tax = income * 0.1
    elif 9876 <= income <= 40125:
        tax = 988 + (income - 9875) * 0.12
    elif 40126 <= income <= 85525:
        tax = 4617 + (income - 40125) * 0.22
    else:
        tax = 14605 + (income - 85525) * 0.24

    return int(round(tax, 0))

def task_1():
    incomes = [[21000, 52000],
               [16000, 32000],
               [8000, 93000],
               [71000, 10000]]

    taxes = []
    for household in incomes:
        household_taxes = []
        for person in household:
            household_taxes.append(tax_calculator(person))
        taxes.append(household_taxes)

    families = ["Takács", "Lukács", "Szabó", "Szatócs"]
    for i in range(len(taxes)):
        print(f"A {families[i]} család {taxes[i][0] + taxes[i][1]} USD adót fizet.")


def task_2():
    my_list = []
    for num in range(1, 11):
        my_list.append(num)
    print(my_list)
    my_list2 = [0 for x in range(1, 11)]
    print(my_list2)


def even_numbers():
    my_list = [num for num in range(100) if num % 2 == 0]
    print(my_list)
    my_list2 = [num for num in range(0, 100, 2)]
    print(my_list2)


def matrix_comprehension():
    zero_matrix = [[0 for i in range(5)] for j in range(5)]
    for row in zero_matrix:
        print(row)

    print()

    matrix1 = [[i for i in range(5)] for j in range(5)]  # i: oszlop index, j: sor index
    for row in matrix1:
        print(row)

    print()

    matrix2 = [[j for i in range(5)] for j in range(5)]
    for row in matrix2:
        print(row)

    print()

    matrix3 = [[j * 5 + i for i in range(5)] for j in range(5)]
    for row in matrix3:
        print(row)

    print()

    matrix4 = [[(j * 5 + i) ** 2 for i in range(5)] for j in range(5)]
    for row in matrix4:
        print(row)

matrix_comprehension()