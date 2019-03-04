def ifEven(n):
    return n/2

def ifOdd(n):
    return (3*n) + 1

def howManyStepsToOne(n):
    steps = 0
    while(n != 1):
        if n % 2 == 0:
            n = ifEven(n)
        else:
            n = ifOdd(n)
        steps += 1

    return steps

#slow but work under one minute on my old laptop
#It can be done much faster by using a modified Erastotelesa Sieve.

const = 1_000_000

def main():
    longestChain = -1
    indexOfLongestChain = -1

    for i in range(1, const + 1):
        iLenght = howManyStepsToOne(i) + 1

        if iLenght > longestChain:
            indexOfLongestChain = i
            longestChain = iLenght

    
    print("index:", indexOfLongestChain)
    print("lenght", longestChain)


if __name__ == "__main__":
    main()