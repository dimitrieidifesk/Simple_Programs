n = 1
cnt = 0
mass = []
while n != 0:
    n = int(input())
    mass.append(n)
for i in mass:
    if i == max(mass):
        cnt += 1
print (cnt)




