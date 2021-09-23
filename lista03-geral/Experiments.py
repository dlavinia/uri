n = int(input())
exp = []
sapos  = 0 
ratos = 0
coelhos = 0
total= 0

for x in range(n):
    exp = input().split()
    qtd = exp[0]
    
    if exp[1] == 'C':
        coelhos += int(qtd)
        
    if exp[1] == 'R':
        ratos += int(qtd)

    if exp[1] == 'S':
        sapos += int(qtd)
    
    total += int(qtd)

pcC = (coelhos*100)/total
pcS = (sapos*100)/total
pcR = (ratos*100)/total

print("Total:", total ,"cobaias")
print("Total de ratos:", ratos)
print("Total de sapos:", sapos)
print("Total de coelhos:", coelhos)
print("Percentual de coelhos: ", "{:.2f}".format(pcC), " %")
print("Percentual de ratos: ", "{:.2f}".format(pcR), " %")
print("Percentual de sapos: ", "{:.2f}".format(pcS), " %")