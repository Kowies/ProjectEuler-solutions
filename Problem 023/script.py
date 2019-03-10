from sympy import divisors

def sumOfProperDividers(number):
    list_of_dividers = divisors(number)

    sum_of_dividers = sum(list_of_dividers)
    sum_of_proper_dividers = sum_of_dividers - number

    return sum_of_proper_dividers


def isAbundant(number):
    if sumOfProperDividers(number) > number:
        return True
    return False 

LIMIT = 28124

def main():
    list_of_abudant_less_than_LIMIT = []

    for i in range(1, LIMIT):
        if isAbundant(i):
            list_of_abudant_less_than_LIMIT.append(i)

    can_be_written_as_the_sum_of_two_abundant_numbers = [False] * LIMIT

    for a in list_of_abudant_less_than_LIMIT:
        for b in list_of_abudant_less_than_LIMIT:
            if a+b < LIMIT:
                can_be_written_as_the_sum_of_two_abundant_numbers[a+b] = True
            else:
                break

    result = 0
    for i in range(1, LIMIT):
        if can_be_written_as_the_sum_of_two_abundant_numbers[i] == False:
                result += i

    print(result)

if __name__ == "__main__":
    main()