a = int(input())
b = int(input())

if b < a:
    aux = a
    a = b
    b = aux

for i in range(a+1,b):
    if i%5==2 or i%5==3:
        print(i)