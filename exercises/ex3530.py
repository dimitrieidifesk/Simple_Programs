n = int(input())

mini = int('1'+'0'*(n-1))
maxi = int('9'*n)

res = []
for i in range(maxi, mini, -1):
    if i % 2 != 0:
        res.append(i)

print (str(res)[1:-1])


