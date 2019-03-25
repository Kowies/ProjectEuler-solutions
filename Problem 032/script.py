from itertools import repeat
from math import log10, floor

def is_good(multiplicand, multiplier, product):
    a = multiplicand
    b = multiplier
    c = product

    str_a = str(a)
    str_b = str(b)
    str_c = str(c)

    temp = str_a + str_b + str_c

    if "".join(sorted(temp)) == "123456789":
        return True
    return False


def len_of_number(number):
    return floor(log10(number)) + 1


def main():
    UPPER_LIMIT = 100000
    result = 0

    products = set()
    
    #i > j
    for i in range(1, UPPER_LIMIT):
        for j in range(1, i):
            k = i * j
            #for faster calculation
            if len_of_number(i) + len_of_number(j) + len_of_number(k) > 9:
                break

            if is_good(i, j, k):
                products.add(k)

    for product in products:
        result += product

    print("result:", result)

if __name__ == "__main__":
    main()