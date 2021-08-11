a, b, c = map(int, input().split())

if a < b and b < c:
    print(a)
    print(b)
    print(c)

if b < a and a < c:
    print(b)
    print(a)
    print(c)

if c < a and a < b:
    print(c)
    print(a)
    print(b)

if a < c and c < b:
    print(a)
    print(c)
    print(b)

if b < c and c < a:
    print(b)
    print(c)
    print(a)

if c < b and b < a:
    print(c)
    print(b)
    print(a)

print("")
print(a)
print(b)
print(c)

