a = input()
#a = a.split('f')
first = a.index("f")
last = len(a[:first+1]) + a[first+1::].index("f")

print (first, last)




