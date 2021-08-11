c1, q1, p1 = input().split()

c2, q2, p2 =input().split()

q1 = int(q1)
q2 = int(q2)

p1= float (p1)
p2 = float (p2)

v = (q1*p1) + (q2*p2)

print("VALOR A PAGAR: R$ " "{:.2f}".format(v))