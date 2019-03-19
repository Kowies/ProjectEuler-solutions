POWER = 5

def is_good(number):
    number_as_str = str(number)
    sum_of_fifth_powers_of_digits = 0

    for digit in number_as_str:
        digit = int(digit)
        sum_of_fifth_powers_of_digits += digit ** POWER

    if sum_of_fifth_powers_of_digits == number:
        return True
    return False


def main():


    LIMIT = 1_000_001 #easy to prove for power 5

    result = 0
    for i in range(10, LIMIT):
        if is_good(i):
            result += i

    print("result:", result)

if __name__ == "__main__":
    main()