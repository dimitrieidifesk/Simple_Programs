n = int(input())
x = float(input())
summa = 1
b_prev = 1
summa = b_prev
for i in range(1,n):
    b_cur = b_prev*x
    summa = summa + b_cur
    b_prev = b_cur   
print (summa)