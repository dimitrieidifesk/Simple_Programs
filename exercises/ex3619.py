a = float(input())
b = float(input())
c = float(input())  
if a == 0:
    if b == 0 and c == 0:
        print(3)
    if b != 0 and (c!= 0 or c == 0):
        x1 = -(c/b)
        print(1,x1)
    if b == 0 and c != 0:
        print(0)
else:
    D = ((b) ** 2) - (4 * a * c)
    if D > 0:
        x2 = ((-b)-(D**0.5))/(2*a)
        x3 = ((-b)+(D**0.5))/(2*a)
        if x2<x3:
            x3,x2 = x2,x3
        print(2,x3,x2)
    elif D == 0:
        x4 = (-b)/(2 * a)
        print(1,x4)
    elif D < 0:
        print(0)




