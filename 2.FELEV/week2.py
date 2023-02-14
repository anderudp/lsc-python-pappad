
def recursion(num):
    print(num)
    if num > 0:
        num -= 1
        recursion(num)

def factorial(num):
    if num == 1:
        return 1
    else:
        return factorial(num-1) * num

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

def harmonic_sum(num):
    if num == 1:
        return 1
    else:
        return 1/num + harmonic_sum(num - 1)

def power(a, b):
    if b == 1:
        return a
    elif a == 0:
        return 0
    elif b == 0:
        return 1
    else:
        return a * power(a, b-1)

def pascal_triangle(rows):
    if rows == 0:
        return []
    elif rows == 1:
        return [1]
    else:
        next_row = [1]
        prev_row = pascal_triangle(rows - 1)
        for i in range(0, len(prev_row) - 1):
            next_row.append(prev_row[i] + prev_row[i+1])
        next_row += [1]
    return next_row

for i in range(1, 10):
    print(pascal_triangle(i))