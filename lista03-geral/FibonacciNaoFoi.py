#ta certo mas deu limite de tempo :C
def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
n = int(input())
lista = []
while n > 0:
    lista.append(fibo(n))
    n= n-1
lista_ok = lista.reverse()

print(*lista, " ")
    