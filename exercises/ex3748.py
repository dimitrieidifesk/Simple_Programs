a = input()
for i in range(len(a)):
    if i % 3 == 0:
        a = a.replace(a[i],"*",1)
a = a.replace('*','')
print (a)




