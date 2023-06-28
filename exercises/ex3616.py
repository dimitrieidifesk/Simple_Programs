p = int(input())
x = int(input())
y = int(input())
k = int(input())

cash = 100 * x + y
for i in range(k):
    cash += int(cash * p / 100)
print(cash // 100, cash % 100)




