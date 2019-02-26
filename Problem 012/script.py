from sympy import divisors

const = 500

def main():
    i = 1
    sumOfAll = 0
    while True:
        sumOfAll += i
        numberOfDivisors = len(divisors(sumOfAll) )

        if numberOfDivisors > const:
            break

        i += 1

    print(sumOfAll)


if __name__ == "__main__":
    main()