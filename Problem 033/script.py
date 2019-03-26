from math import isclose, gcd

def is_good(numerator, denumerator):

    str_numerator = str(numerator)
    str_denumerator = str(denumerator)

    for digit in range(1, 10):
        temp_numerator = str_numerator.replace(str(digit), "")
        temp_denumerator = str_denumerator.replace(str(digit), "")

        if temp_numerator == "" or temp_denumerator == "":
            continue
        if (temp_numerator == str_denumerator 
                or temp_denumerator == str_denumerator):
            continue
        if temp_denumerator == "0":
            continue

        value = numerator / denumerator
        new_value = int(temp_numerator) / int(temp_denumerator)

        if isclose(value, new_value):
            return True

    return False


def main():

    corect_fraction = []

    for denumerator in range(10,100):
        for numerator in range(10, denumerator):
            if is_good(numerator, denumerator):
                corect_fraction.append((numerator, denumerator))


    product_of_numerators = 1
    product_of_denumerator = 1

    for numerator, denumerator in corect_fraction:
        product_of_numerators *= numerator
        product_of_denumerator *= denumerator

    result = product_of_denumerator // gcd(product_of_numerators, 
        product_of_denumerator)

    print(result)

if __name__=="__main__":
    main()