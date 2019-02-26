from sympy import sieve

const = 2_000_000

def main():
    result = 0
    for prime in sieve.primerange(2, const + 1):
        result += prime

    print(result)

if __name__ == "__main__":
    main()