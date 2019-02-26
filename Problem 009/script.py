from math import sqrt

def isPythagoreanTriplet(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    return False


def main():
    for i in range(1001):
        for j in range(i + 1, 1001):
            k = round(sqrt(i**2 + j**2))
            if k > j:
                if i**2 + j**2 == k**2:
                    if i + j + k == 1000:
                        print(i, j, k)
                        print(i * j * k)

if __name__ == "__main__":
    main()