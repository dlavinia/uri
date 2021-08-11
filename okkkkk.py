a, b = map(float, input().split())
c = b-a

p  = c*100/a

print("{:.2f}".format(p), "%" , sep=(""))