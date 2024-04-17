n = int(input())

a = []
b = []
c = []
for i in range(1,n+1):
    a.append(0)

for i in range(1,n+2):
    b.append(1)

for i in range(1,2*n+2):
    if i%2 != 0 :
        c.append(1)
    else :
        c.append(0)

c = [str(n) for n in c]

print(''.join(c))



