cnt1 = int(input())
cnt2 = int(input())
cnt3 = int(input())
if cnt1 % 2 == 0:
    res1 = cnt1 // 2
else:
    res1 = (cnt1+1) // 2
if cnt2 % 2 == 0:
    res2 = cnt2 // 2
else:
    res2 = (cnt2+1) // 2
if cnt3 % 2 == 0:
    res3 = cnt3 // 2
else:
    res3 = (cnt3+1) // 2

print (res1+res2+res3)



