from sympy import divisors

def d(number):
    list_of_divisors = divisors(number)
    return sum(list_of_divisors) - number

const = 10000

def main():
    result = 0
    for a in range(2, const+1):
        b = d(a)
        if d(b) == a:
            if a != b:
                result += a

    print("result:", result)

if __name__ == "__main__":
    main()