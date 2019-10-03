import math
def Q(D):
    C=50
    H=30
    return (int(math.sqrt((2*C*D)/H)))

a=input()
y=a.split(',')
z=[str(Q(int(y[i]))) for i in range(len(y))]
s=","
s=s.join(z)
print(s)


