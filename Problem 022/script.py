def valueOfName(name: str) -> int: 
    result = 0

    for letter in name:
        value = ord(letter) - ord("A") + 1
        result += value

    return result

def main():

    with open("names.txt") as file:
        raw_data = file.readline()

    raw_data = raw_data.replace('"',"")

    names = raw_data.split(",")
    names.sort()

    result = 0
    for index, name in enumerate(names, 1):
        result += index * valueOfName(name)

    print(result)

if __name__ == "__main__":
    main()