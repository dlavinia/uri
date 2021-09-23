n = int(input())
k = int(input())
listpts = []
clas = 0
for x in range(0 , n):
    pontuacao = int(input())
    listpts.append(pontuacao)

listpts.sort(reverse = True)
ultimoCla = listpts[k-1]
repeticoes =0

for x in range(k, len(listpts)):
    if listpts[x] == ultimoCla:
        repeticoes=repeticoes+1
        print("repetiu ultimo clas", ultimoCla)
     
clas = k + repeticoes
print(clas)