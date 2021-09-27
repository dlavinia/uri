while True:
    
    n = int(input())
    if n !=0:
        r = ''

        for x in range(1, n+1):
            
            r += str(x) + " "
        print(r[:-1])

    else:
        break
    