const = 1000

def main():
    number = 2 ** const
    result = 0

    for digit in str(number):
        result += int(digit)

    print(result)

if __name__ == "__main__":
    main()