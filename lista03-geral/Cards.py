listaini = list(map(int, input().split()))

listaCres = sorted(listaini)

listaDecres = sorted(listaini, reverse = True)

c = 0
d = 0

for x in range (0, 5):
    if listaini[x] == listaCres[x]:
        c = c+1
    if listaini[x] == listaDecres[x]:
        d = d+1
if c == 5:
    print("C")

elif d == 5:
    print("D")

else:
    print("N")

