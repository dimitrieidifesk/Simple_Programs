n = int (input())
h = n // 60
m = n - (h*60)
if h > 23:
    h = h - 24
if m > 59:
    m = m - 60
print (h,m)



