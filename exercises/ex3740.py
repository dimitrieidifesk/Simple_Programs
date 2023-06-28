a = input()
if 'f' in a:
    first = a.index("f")
    if 'f' in a[first+1::]:
        second =len(a[:first+1]) + a[first+1::].index("f")
    else:
        second = -1
else:
    second = -2
print (second)



