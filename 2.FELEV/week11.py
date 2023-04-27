scores = []
for i in range(5):
    scores.append(int(input("Add meg a következő pontszámot: ")))

class_tuples = []
for score in scores:
    if score >= 85:
        class_tuples.append((score, 5))
    elif score >= 70:
        class_tuples.append((score, 4))
    elif score >= 55:
        class_tuples.append((score, 3))
    elif score >= 40:
        class_tuples.append((score, 2))
    else:
        class_tuples.append((score, 1))

class_tuples = tuple(class_tuples)


minimum = class_tuples[0][0]
maximum = class_tuples[0][0]
for score_tuple in class_tuples:
    if score_tuple[0] > maximum:
        maximum = score_tuple[0]
    elif score_tuple[0] < minimum:
        minimum = score_tuple[0]
print(f"A legkisebb pontszám {minimum}, a legnagyobb {maximum}")


average_score = 0
average_grade = 0
sum_score = 0
sum_grade = 0
for score_tuple in class_tuples:
    sum_score += score_tuple[0]
    sum_grade += score_tuple[1]

average_score = sum_score / len(class_tuples)
average_grade = sum_grade / len(class_tuples)
print(f"Az osztályátlag {average_grade}, {average_score} pontszámmal.")

# 2.feladat: Szimmetrikus tuple
test_tuples = [(6, 7, 6), (5, 4), (3, 3, 3), (1, 3, 18), (19, 6, 6, 19), (17, 3, 1, 4, 1, 3, 19)]
symmetric = []
for test_tuple in test_tuples:
    if test_tuple[::-1] == test_tuple:
        symmetric.append(test_tuple)
print(f"A szimmetrikus tuple-ök: {symmetric}")


# 3.feladat: Tuple -> String
test_tuples = [(6, 7, 6), (5, 4), (3, 3, 3), (1, 3, 18), (19, 6, 6, 19), (17, 3, 1, 4, 1, 3, 19)]
print("Eredeti lista:", str(test_tuples))
result_string = ""
for test_tuple in test_tuples:
    for num in test_tuple:
        result_string += str(num) + ", "
print("Tuple lista stringként:", result_string)

