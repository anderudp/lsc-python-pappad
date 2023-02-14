
def print_hello():
    print("Üdv a 2.félévben!")


def is_prime(number):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
    if prime:
        print("A", number, "szám prím.")
    else:
        print("A", number, "szám nem prím.")


def is_right_triangle(a, b, c):
    if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        print("A háromszög derékszögű.")
    else:
        print("A háromszög nem derékszögű.")


def func_numbers(p, q, r):
    print(p + q**2 + r**3)


def absolute_value(number):
    if number >= 0:
        return number
    else:
        return -number


def mpg_to_l100(miles_per_gallon):  # Mérföld/gallon -> Liter/100km
    km = miles_per_gallon * 1.609344
    liter = 3.785411
    return liter/100*km


def l100_to_mpg(liter_per_100km): # Liter/100km -> Mérföld/gallon
    gallon = liter_per_100km / 3.785411
    miles = 100/1.609344
    return miles/gallon


def exit_function():
    for i in range(1, 11):
        if i >= 5:
            return "A program véget ért."
        print(i)

print(exit_function())