a = float(input())
h = 30
m = h/60
s = m/60

h = (a//h)%60
m = (a//m)%60
s = (a//s)%60
print(h, m, s)




