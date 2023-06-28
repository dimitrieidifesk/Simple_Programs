a = input()
a = a.replace('#', '')
s1 = ' '
s2 = ' '
cnt = 0
for i in a:
    cnt += 1
    if (cnt % 2 == 1):
        s1 += i
    else:
        s2 = i + s2
print(s1+s2)


