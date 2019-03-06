from num2words import num2words

const = 1000

def main():
    result = 0

    for i in range(1, const + 1):
        numberName = num2words(i)
        numberNameWithoutSpacesAndHyphens = numberName.replace(" ","").replace("-","")
        print(numberName, numberNameWithoutSpacesAndHyphens)
        result += len(numberNameWithoutSpacesAndHyphens)

    print(result)

if __name__ == "__main__":
    main()