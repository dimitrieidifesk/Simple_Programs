n1=int(input())
n2=int(input())

if n2 > n1:
    n1, n2 = n2, n1

while ( True ):
    a=int(input())
    if a == 0:
        break
    if a > n1:
        n1, n2 = a, n1
    elif a > n2:
        n2 = a

print(n2)



