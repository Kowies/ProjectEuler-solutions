import math

def fibonacci():
    a,b = 1, 1

    while True:
        yield a
        b, a = a + b, b

def len_of_number(number):
    if number > 0:
        return math.floor(math.log10(number)) + 1
    raise Exception() 

def main():
    DIGITS = 1000

    for index, number in enumerate(fibonacci(), 1):
        how_many_digit = len_of_number(number)
        if how_many_digit == DIGITS:
            result = index
            break

    print("result:", result)
        
if __name__ == "__main__":
    main()