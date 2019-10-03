a=input()
y=a.split(',')
lt=[[0 for i in range(int(y[1]))] for j in range(int(y[0]))]
for i in range(int(y[0])):
    for j in range(int(y[1])):
        lt[i][j]=i*j
print(lt)