d = int(input())

a, b, c=  map(int, input().split())

n = (a*b*c)

v =  (4 * 3.14 * (d/2)* (d/2)* (d/2))/3

if (v <= n):
    print ("S")

else:
    print("N")

print (v, n)

