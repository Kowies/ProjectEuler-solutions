from itertools import permutations

def main():
    elements = list(range(10))
    WHICH = 1_000_000
    all_perm = permutations(elements)

    i = 1
    for perm in all_perm:
        if i == WHICH:
            break
        i += 1

    str_perm = [str(x) for x in perm]
    result = "".join(str_perm) 
    print(result)


if __name__ == "__main__":
    main()