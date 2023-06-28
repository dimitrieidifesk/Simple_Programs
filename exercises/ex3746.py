a = input()
l=a.split('h')
l1 = 'h'.join(l[1:-1])
l1 = l1.replace('h','H')
print (f'{l[0]}h{l1}h{l[-1]}')




