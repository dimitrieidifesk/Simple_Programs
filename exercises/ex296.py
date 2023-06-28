a = int(input())
b = int(input())
c = int(input())
values = [a,b,c]
counter = {}
 
for elem in values:
    counter[elem] = counter.get(elem, 0) + 1
 
doubles = [count for element, count in counter.items() if count > 1]

if doubles != []: print (doubles[0]) 
else: print (0)
    


