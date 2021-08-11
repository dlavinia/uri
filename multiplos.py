a, b = map(int, input().split())

if a > b and a%b == 0:
    print("are multiples")

elif b > a and b%a==0:
    print("are multiples")

elif a==b:
    print("are multiples")
    
else:
    print("aren’t multiples")