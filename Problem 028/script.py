
def main():
    SIDE = 1001

    if SIDE % 2 != 1:
        raise Exception()

    table = {}

    x = 0
    y = 0
    next_number = 1
    table[x, y] = next_number
    next_number += 1

    def go_left(i):
        nonlocal x, y, next_number
        for i in range(i):
            x -= 1 
            table[x, y] = next_number
            next_number += 1

    def go_right(i):
        nonlocal x, y, next_number
        for i in range(i):
            x += 1
            table[x, y] = next_number
            next_number += 1

    def go_up(i):
        nonlocal x, y, next_number
        for i in range(i):
            y += 1
            table[x, y] = next_number
            next_number += 1

    def go_down(i):
        nonlocal x, y, next_number
        for i in range(i):
            y -= 1
            table[x, y] = next_number
            next_number += 1

    for i in range(1, (SIDE-1), 2):
        go_right(1)

        go_down(i)

        go_left(i+1)

        go_up(i+1)

        go_right(i+1)

    result = 0

    result += table[0,0]

    for i in range(1, (SIDE-1)//2 + 1):
        result += table[i, i]
        result += table[-i, i]
        result += table[-i, -i]
        result += table[i, -i]

    print(result)

if __name__ == "__main__":
    main()