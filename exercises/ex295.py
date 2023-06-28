a = int(input())
b = int(input())
c = int(input())

if a+b > c:
    if a+c > b:
        if b+c > a:
            print ("YES")
        else:
            print ('NO')
    else:
        print ('NO')
else:
    print ('NO')

