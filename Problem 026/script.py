import itertools

def length_of_recurring_cycle(a, b):
    if a >= b:
        a %= b

    rest = a
    in_which_iteration_was_that_value_of_rest = {}

    for i in itertools.count(1):
        rest *= 10
        if rest in in_which_iteration_was_that_value_of_rest:
            return (i - in_which_iteration_was_that_value_of_rest[rest])
        in_which_iteration_was_that_value_of_rest[rest] = i
        rest %= b
        if rest == 0:
            return 0

def main():

    LIMIT = 1000    

    lenght_of_max = 0
    index_of_max = 1

    for index in range(2, LIMIT):
        length = length_of_recurring_cycle(1, index)
        if length > lenght_of_max:
            lenght_of_max = length
            index_of_max = index

    result = index_of_max

    print("result:", result)    


if __name__ == "__main__":
    main() 
