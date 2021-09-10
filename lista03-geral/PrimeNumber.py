x = int(input())

for i in range(x):

    n = int(input())
    div = 1

    for i in range(1,n):
        if (n%i)==0 or n==i:
            div = div+1
    
    if div > 2:
        print(n, "não é primo")
    else:
        print(n, "é primo")
                