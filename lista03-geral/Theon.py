n = int(input())
t = list(map(int, input().split()))

menor = min(t)
indice = t.index(menor)

print(indice+1)