from sympy import isprime

from itertools import count

def how_many_primes(a, b, c):

    f = lambda x: a*x**2 + b*x + c

    result = 0
    for x in count():
        y = f(x)
        #slow but sufficient
        if not isprime(y):
            return result
        result += 1

def main():

    print("Wait 5-10 sec...")
    FROM = -999
    TO = 1000

    a_of_max = -1
    b_of_max = -1
    value_of_max = -1

    for a in range(FROM, TO):
        for b in range(FROM, TO):
            value = how_many_primes(1, a, b)
            if value > value_of_max:
                value_of_max = value
                a_of_max = a
                b_of_max = b 

    result = a_of_max * b_of_max

    print("result:", result)

if __name__ == "__main__":
    main()