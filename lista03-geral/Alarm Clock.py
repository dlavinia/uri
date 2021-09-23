
while True:
    h1, m1, h2, m2 = map(int, input().split())
    inicio = 0
    fim = 0
    if m1+m2+h1+h2 == 0:
        break
    if h1 == 0:
        inicio = (24*60)+m1
    else:
        inicio = (h1*60) + m1
    if h2 == 0:
        fim =(24*60)+m2
    else:
        fim = (h2*60) + m2
    if fim > inicio:
        print(fim-inicio)
    else:
        print((24*60)-(inicio-fim))