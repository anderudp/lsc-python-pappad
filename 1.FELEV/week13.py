# 1.Feladat: Két lista metszete
list_1 = [61, 5, 6, 28, 87, 52, 89, 51, 86, 29, 93, 26, 99, 16, 36, 53, 47, 95, 18, 54, 62, 37, 34, 11, 75, 90, 88, 24, 72, 76, 55, 44,  3, 50, 35, 17, 94,  7, 31,100, 42, 43, 74, 83, 82,  4, 10]
list_2 = [5, 9, 62, 79, 17, 68, 54, 50, 60, 89, 29, 41, 83, 77,  3, 86, 56, 13, 26, 52, 98, 81, 82, 74, 55, 66, 92, 61, 30, 37, 57, 91,  2, 71, 93, 35, 33, 24,100, 19, 65, 95, 90, 38, 88, 31, 80, 70, 25, 39, 15, 85, 42, 94, 11, 76, 32,  7, 48]
common_values = []
for i in list_1:
    for j in list_2:
        if i == j:
            common_values.append(i)
print(common_values)

# 2.Feladat: Lista számainak egybeforrasztása
numbers = [12, 54, 812]
whole_number = ""
for i in numbers:
    whole_number += str(i)
whole_number = int(whole_number)
print(whole_number)
print(type(whole_number))

# 3.Feladat: Két lista azonossá tétele
list_1 = [43, 70, 25, 39, 15, 85, 42, 94, 11, 76, 20,  36, 48]
list_2 = [36, 44, 20, 96, 69, 15, 27, 14, 87, 67, 97, 43,  8, 22]
print(list_1)
print(list_2)
for i in list_1:
    if i not in list_2:
        list_2.append(i)
for i in list_2:
    if i not in list_1:
        list_1.append(i)
list_1.sort()
list_2.sort()
print(list_1)
print(list_2)

# 4.Feladat: Növekvő-e a lista
my_list = [43, 70, 25, 39, 15, 85, 42, 94, 11, 76, 20, 36, 48]
print(my_list)
is_sorted = True
index = 0
while is_sorted and index < len(my_list)-1:
    if my_list[index] > my_list[index + 1]:
        is_sorted = False
    else:
        index += 1
if is_sorted:
    print("A lista növekvően rendezett.")
else:
    print("A lista nem növekvően rendezett.")

# 6.Feladat: A Fibonacci-sorozat 100.eleme
a_1 = 0
a_2 = 1
series = [a_1, a_2]
for i in range(98):
    series.append(series[-2]+series[-1])
print(series[-1])