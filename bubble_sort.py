a=[1,7,3,2,5,10,4] 
n=len(a)
for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
for i in a:
    print(i)