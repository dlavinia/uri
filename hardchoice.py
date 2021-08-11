a, b, c = map(int, input().split())

a2, b2, c2 = map(int, input().split())

p = 0

if (a < a2):
    p = p + (a2 - a)

if (b < b2):
    p = p + (b2 - b)

if ( c < c2):
    p = p + (c2- c)

print(p)

