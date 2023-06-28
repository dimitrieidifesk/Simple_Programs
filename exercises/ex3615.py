p = int(input())
x = int(input())
y = int(input())
cash = x*100+y
new_cash = cash+(cash*p/100)
rub = int(new_cash // 100)
kop = int(new_cash % 100)
print(rub, kop)


