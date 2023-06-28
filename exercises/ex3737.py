a = input()
half = len(a)//2
print (f"{a[half+len(a)%2::]}{a[:half+len(a)%2]}")



