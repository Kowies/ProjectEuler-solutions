def main():
    A_FROM = 2
    A_TO = 101
    A_RANGE = (2,101)
    B_FROM = 2
    B_TO = 101

    numbers = set()

    for a in range(A_FROM, A_TO):
        for b in range(B_FROM, B_TO):
            x = a**b    # it can be boosted
            numbers.add(x)

    result = len(numbers)
    print("result:", result)

if __name__ == "__main__":
    main()