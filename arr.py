a=input()
b=input()
a=a.split()
b=b.split()
sum=0
for i in range(0,int(a[1])):
    sum=sum+int(b[i])
print(sum)
