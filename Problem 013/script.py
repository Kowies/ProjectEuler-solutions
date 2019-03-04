import pandas as pd

const = 10

def main():
    data = pd.read_csv("data.txt")
    series = data.iloc[:,0]

    sumOfAll = 0

    for index, value in series.iteritems():
        sumOfAll += int(value)

    string = str(sumOfAll)
    print(string)
    print(string[0:const])


if __name__ == "__main__":
    main()