
def factorization(n):

    if  n < 2:
        raise Exception()

    i = 2
    number = n
    result = [] 

    while n != 1:
        if n % i == 0:
            result.append(i)
            n /= i
        else:
            i += 1


    return result

print(factorization(600851475143))
