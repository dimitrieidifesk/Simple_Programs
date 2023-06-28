a = int(input())
b = int(input())


try: 
    x = -(b/a)
    if float(x).is_integer():
        print (int(x))
    else:
        print ('NO')

except: print ('INF')



