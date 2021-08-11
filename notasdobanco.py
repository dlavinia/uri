v = int(input())
print (v)

q100 = v//100

q50 = (v%100)//50

q20 = ((v%100)%50)//20

q10 = (((v%100)%50)%20)//10

q5 = ((((v%100)%50)%20)%10)//5

q2 = (((((v%100)%50)%20)%10)%5)//2

q1 =((((((v%100)%50)%20)%10)%5)%2)//1


print(q100, "nota(s) de R$ 100,00", end="\n")
print(q50, "nota(s) de R$ 50,00", end="\n")
print(q20, "nota(s) de R$ 20,00", end="\n")
print(q10, "nota(s) de R$ 10,00", end="\n")
print(q5, "nota(s) de R$ 5,00", end="\n")
print(q2, "nota(s) de R$ 2,00", end="\n")
print(q1, "nota(s) de R$ 1,00", end="\n")
