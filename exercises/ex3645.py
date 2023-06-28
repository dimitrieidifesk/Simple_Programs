n = int(input())
x = 1
if n == 1:
    print("YES")
elif n % 2 == 0:
    while x < n:
        x *= 2
    else:
        if x == n:
            print('YES')
        elif x > n:
            print('NO')
else:
    print('NO')




