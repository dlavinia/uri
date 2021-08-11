a,b= map(int,input().split())

if(a<b):
    time=b-a

else:
    time=b+24-a
print("O JOGO DUROU", time, "HORA(S)")
