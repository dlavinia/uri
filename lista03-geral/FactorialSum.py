def fatorial(n):
    if n == 0:
        return 1
    else:
        return n*fatorial(n-1)

while True:
    try:
        a, b= map(int, input().split())
        fatA = fatorial(a)
        fatB = fatorial(b)
        soma = fatA + fatB

        print(soma)
        
    except EOFError:
        break