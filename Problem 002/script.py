

def fib(n):

    list = [0, 1]
    i = 2   #len of list

    while n >= list[i-1] + list[i-2]:
        list.append(list[i-1] + list[i-2])
        i += 1

    return list


def isEven(n):
    if n % 2 == 0:
        return True
    return False

const = 4_000_000

result = 0

for n in fib(const):
    if isEven(n):
        result += n

print(fib(const))
print(result)

