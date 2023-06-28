n = int(input())

res_str = ''
res_int = 0
for i in range (2, n + 1):

    res_str += f'{i-1}*{i}'
    res_int += (i-1)*i
    if i != n:
        res_str += ' + '
    else:
        res_str += ' ='

print (res_str, res_int)

