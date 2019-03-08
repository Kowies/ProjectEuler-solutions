from math import factorial

def main():
    number = factorial(100)
    result = 0
    for i in str(number):
        result += int(i)

    print("result:", result)

if __name__ == "__main__":
    main()