while True:
    try:
        n = int(input())
        v = list(map(int, input().split()))

        maior = max(v)

        if maior >= 20:
            print("3")
        elif maior < 10:
            print("1")
        else:
            print("2")
    except EOFError:
        break