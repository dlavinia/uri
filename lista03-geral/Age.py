idade = 0
cont = 0
soma =0
while( idade >= 0):

    idade = int(input())

    if idade > 0:
        soma = soma+idade

        cont = cont+1
    else:
        break

print("%.2f" %(soma/float(cont)))
    