
import math

# 2.feladat
# Írjunk egy függvényt, ami kap 2 számot paraméterként, és visszatéríti az összegüket
def my_sum(x, y):
    return x + y

# 3.feladat
# Írjunk egy függvényt, ami kap 2 számot paraméterként, és visszatéríti az átlagukat
def my_avg(x, y):
    return (x + y) / 2


# 4.feladat
# Írjunk egy függvényt, ami kap 2 számot paraméterként, és visszatéríti a hatványukat
# Az első paraméter a hatványalap, a második a hatványkitevő
def my_pow(x, y):
    return x ** y

# 5.feladat - Prímkereső
def my_prime_finder(p):
    primes = []
    for num in range(2, p):
        is_prime = True
        for div in range(2, math.ceil(math.sqrt(num)) + 1):
            if num % div == 0:
                is_prime = False
                continue
        if is_prime:
            primes.append(num)
    return primes
