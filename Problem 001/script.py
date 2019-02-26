
def isGood(x):
    if (x % 3 == 0) or (x % 5 == 0):
        return True
    return False



result = 0

for i in range(1000):
    if isGood(i):
        result += i


print(result)