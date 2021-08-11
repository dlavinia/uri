a1 = int(input())
a2 = int(input())
a3 = int(input())

t1 = a1*0 + a2*2 + a3*4
t2 = a1*2 + a2*0 + a3*2
t3 = a1*4 + a2*2 + a3*0

if t1 <= t2 and t1 <=t3:
    print(t1)

elif t2 <= t1 and t2 <= t3:
    print(t2)

elif t3 <= t1 and t3 <=t2:
    print(t3)



