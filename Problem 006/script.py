x = 0
y = 0
for i in range(101):
    x += i**2
    y += i
    
y = y**2

print(y-x)
