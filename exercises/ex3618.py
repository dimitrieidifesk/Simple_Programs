a = float(input())
b = float(input())
c = float(input())

d = (b**2)-(4*a*c)
t = 2*a
if d > 0:
    print((-b+(d**(1/2)))/t,(-b-(d**(1/2)))/t)
elif d == 0:
    print(-b/(2*a))




