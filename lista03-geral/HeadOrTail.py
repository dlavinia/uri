while True:
    n = int(input())

    if (n == 0):
        break

    resultados = list(map(int,input().split()))
    mary = 0
    john = 0
    for v in resultados:
        if(v == 0):
            mary += 1
        else:
            john += 1
        
    print("Mary venceu", mary, "vezes e John venceu" ,john, "vezes")
        
    