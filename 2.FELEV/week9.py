# 1.feladat - Eddig ismert operátorok
def arithmetic_operators():
    print(3 + 4)
    print(3 - 4)
    print(3 / 4)
    print(3 * 4)
    print(3 ** 4)
    print(3 // 4)
    print(3 % 4)


def logic_operators():
    rozi_ate_apples = True
    gyuri_drank_milk = False
    print(rozi_ate_apples or gyuri_drank_milk)


# 2.feladat: 2-es számrendszer (bináris)
def binary_conversion():
    print(bin(8))
    print(bin(186)[2:])


# 3.feladat: bitoperátorok
def bitwise_operators():
    a = 1
    b = 1
    print(a & b)
    print(a | b)
    print(a ^ b)

    print()

    a = 78
    b = 120
    print(bin(a))
    print(bin(b))
    print(a & b)
    print(a | b)
    print(a ^ b)

    print()

    a = 3
    b = 63
    print(bin(a))
    print(bin(b))
    print(a & b)
    print(a | b)
    print(a ^ b)


# 4.feladat: bit shiftelés
def bit_shift():
    print(bin(64))
    print(64 >> 2)  # eltolás jobbra 2-vel
    print(64 << 3)

bit_shift()