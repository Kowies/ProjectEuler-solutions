def indexIsGood(index):
    i = index[0]
    j = index[1]

    if i >= 0 and j >= 0:
        if i >= j:
            return True

    return False


def main():
    data = []
    with open("data.txt") as input_file:
        for line in input_file:
            good_list = [int(x) for x in line.split(" ")]
            data.append(good_list)

    maxSumTo = data

    #dynamic programing
    for i, line in enumerate(data):
        for j, value in enumerate(line):
            index_top_left = (i-1, j-1)
            index_top_right = (i-1, j)

            value_top_left = 0
            if indexIsGood(index_top_left):
                x = index_top_left[0]
                y = index_top_left[1]
                value_top_left = maxSumTo[x][y]

            value_top_right = 0
            if indexIsGood(index_top_right):
                x = index_top_right[0]
                y = index_top_right[1]
                value_top_right = maxSumTo[x][y]

            maxSumTo[i][j] += max(value_top_left, value_top_right)


    result = max(data[-1])

    print("result:", result)

if __name__ == "__main__":
    main()