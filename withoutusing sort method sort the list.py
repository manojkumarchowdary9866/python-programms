l=[1,4,6,2,5,3]
h=l[0]
l1=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print(l)
