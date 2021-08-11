x = int(input())
a, b, c, d, e = map(int, input().split())

acertos = 0

if a == x:
    acertos = acertos + 1

if b == x:
    acertos = acertos + 1

if c == x:
    acertos = acertos + 1

if d == x:
    acertos = acertos + 1

if e == x:
    acertos = acertos + 1

print(acertos)