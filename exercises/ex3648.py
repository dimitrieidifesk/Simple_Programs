x = int(input())
p = int(input())
y = int(input())

year = 0
while x < y:
    x += ((x/100)*p)
    year += 1

print (year)

