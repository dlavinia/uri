a, b, c = map(int, input().split())

if a == b+c or b == a+c or c == a+b or a == b-c or a== c-b or b== a-c or b== c-a or c== a-b or c== b-a or a == b or c==b or a==c:
    print ("S")
else:
    print("N")