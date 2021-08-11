n1, n2, n3, n4 = map(float, input().split())

media = ((n1*2)+(n2*3)+(n3*4)+n4)/10

if(media >= 7.0):
    print("Aluno aprovado.")

if(media < 5.0):
    print("Aluno reprovado.")

if(media >= 5.0 and media <= 6.9):
    print("Aluno em exame.")
    
    nota_exame = float(input())
    print("Nota do exame: %.1f" %nota_exame)
    media = (media + nota_exame)/2
    
    if(media >= 5.0):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print('Media final: %.1f' %media)
    
        