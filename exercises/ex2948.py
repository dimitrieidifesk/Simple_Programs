#h:mm:ss
n = int(input())
if n<86400:
    h = n//3600
    m = n//60
    s = n%60
else:
    h = (n % 86400) // 3600
    m = (n % 86400) // 60
    s = (n % 86400) % 60

if h > 23:
    h = h - 24
if m > 59:
    m = m % 60
if len(str(m)) == 1:
    m = f"0{m}"
if s > 59:
    s = s - 60
if len(str(s)) == 1:
    s = f"0{s}"

print (f"{h}:{m}:{s}")


