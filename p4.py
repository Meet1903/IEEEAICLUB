s1=input()
l1=s1.split(' ')
d1={}
for i in l1:
    d1[i]=l1.count(i)
for i,j in zip(d1.keys(),d1.values()):
    print(i,":",j)
