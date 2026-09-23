a=[1,4,2,5,6]
x=int(input("enter element to search"))
for i in a:
    if i == x:
        flag=True
        break
    else:
        flag=False
if flag==True:
    print("element found")
else:
    print("element not found")