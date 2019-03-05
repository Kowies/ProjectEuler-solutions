import numpy as np

const = 21

def main():
    # In this array we write down the number of possible routes for a given 
    # point.
    howManyDifferentPathsTo = np.zeros((const, const), int)

    howManyDifferentPathsTo[(0, 0)] = 1 #we know it

    for index, value in np.ndenumerate(howManyDifferentPathsTo):
        indexAbove = (index[0]-1, index[1])
        indexOnTheLeft = (index[0], index[1]-1)
       
        if indexAbove[0] >= 0 and indexAbove[1] >= 0:
            howManyDifferentPathsTo[index] += howManyDifferentPathsTo[indexAbove]

        if indexOnTheLeft[0] >= 0 and indexOnTheLeft[1] >= 0:
            howManyDifferentPathsTo[index] += howManyDifferentPathsTo[indexOnTheLeft]


    indexOfBottomLeft = (const-1, const-1)
    answer = howManyDifferentPathsTo[indexOfBottomLeft]
    print(answer)


if __name__ == "__main__":
    main()