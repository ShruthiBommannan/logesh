n=int(input())
k=int(input())
a=[]
for i in range(1,n+1):
    a.append(i)

l=0
for i in range(0,k):
    l=l+a[i]
print(l)
