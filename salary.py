c, h, v = input().split()

h = int(h)
v = float(v)
s= h*v

print ("NUMBER =", c, end=("\n"))
print ("SALARY = U$", "{:.2f}".format(s),  end=("\n"))