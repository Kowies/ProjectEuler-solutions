from sympy.ntheory import factorint

factoredResult = {}

for i in range(2, 21):
    factored = factorint(i)
    for key, value  in factored.items():
        if factoredResult.get(key, 0) < value:
            factoredResult[key] = value



result = 1

for key, value in factoredResult.items():
    result *= key**value


print(result)