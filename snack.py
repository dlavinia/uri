x, y = map(int, input().split())



if x == 1:
 p = 4.00

elif x == 2:
 p = 4.50

elif x == 3:
 p = 5.00

elif x == 4:
 p = 2.00

elif x == 5:
 p = 1.50

t = p*y
print("TOTAL: R$", "{:.2f}".format(t))

