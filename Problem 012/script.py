import numpy as np

def mulOfFour(data, coordinate, directory):
    y = coordinate[0]
    x = coordinate[1]
    result = 1

    if directory == "down":
        for i in range(4):
            result *= data[y+i][x]
        return result

    if directory == "right":
        for i in range(4):
            result *= data[y][x+i]
        return result

    if directory == "diagonallyRD":
        for i in range(4):
            result *= data[y+i][x+i]
        return result

    if directory == "diagonallyLD":
        for i in range(4):
            result *= data[y+i][x-i]
        return result

    raise Exception("wrong directory")


def main():
    data = np.loadtxt("data.txt", int)

    maxDown = -1
    for i in range(0, 17):
        for j in range(0, 20):
            newValue = mulOfFour(data, (i,j), "down")
            maxDown = max(newValue, maxDown)

    maxRight = -1
    for i in range(0, 20):
        for j in range(0, 17):
            newValue = mulOfFour(data, (i,j), "right")
            maxRight = max(newValue, maxRight)

    maxDiagonallyRD = -1
    for i in range(0, 17):
        for j in range(0, 17):
            newValue = mulOfFour(data, (i,j), "diagonallyRD")
            maxDiagonallyRD = max(newValue, maxDiagonallyRD)

    maxDiagonallyLD = -1
    for i in range(0, 17):
        for j in range(3, 20):
            newValue = mulOfFour(data, (i,j), "diagonallyLD")
            maxDiagonallyLD = max(newValue, maxDiagonallyLD)

    print("maxDown:", maxDown)
    print("maxRight:", maxRight)
    print("maxDiagonallyRD:", maxDiagonallyRD)
    print("maxDiagonallyLD:", maxDiagonallyLD)

    print("max", max(maxDown, maxRight, maxDiagonallyRD, maxDiagonallyLD) )

if __name__ == "__main__":
    main()