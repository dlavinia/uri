a, b, c = map(int, input().split())

l, h= map(int, input().split())

if  (a <= l and b <= h) or (a <= l and c <= h) or (b <= l and c <= h) or (b <= l and a <= h) or (c <= l and a <= h) or (c <= l and b <= h):
    print ("S")

else:
    print ("N")