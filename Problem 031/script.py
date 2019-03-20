import numpy as np

class DynamicProblem():

    denominations = [1, 2, 5, 10, 20, 50, 100, 200]

    def __init__(self, LIMIT):
        self.value = np.zeros((LIMIT, LIMIT), int)
        self.is_calculed = np.zeros((LIMIT, LIMIT), bool)

        for i in range(LIMIT):
            self.value[0, i] = 1
            self.is_calculed[0, i] = True

    def __getitem__(self, key):

        if self.is_calculed[key] == True:
            return self.value[key]

        sought_sum, smallest_allowed_denomination = key
        result = 0

        allowed_denominations = [denomin for denomin in self.denominations 
            if denomin >= smallest_allowed_denomination and denomin <= sought_sum ]

        for denomin in allowed_denominations: 
            result += self[sought_sum - denomin,
                max(smallest_allowed_denomination, denomin)]

        self.value[key] = result
        self.is_calculed[key] = True
        return result


def main():
    d = DynamicProblem(201)

    result = d[200, 0] #sought_sum = 200, smallest_allowed_denomination = 0

    print("result:", result)

if __name__ == "__main__":
    main()