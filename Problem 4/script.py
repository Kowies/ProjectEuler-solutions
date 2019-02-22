
def isPalindrom(n):

    string = str(n)
    reversed_string = string[::-1]

    if string == reversed_string:
        return True
    return False


first = 100
last = 999

max = -1

for x, y  in [(a, b) for a in range(first, last) for b in range(first, last)]:
    if isPalindrom(x * y):
        if max < x*y:
            max = x*y
            print(x, y, x*y)

