a,b = [int(input()) for i in range(2)]
c = a

while c % b:
    c += a
print(c)