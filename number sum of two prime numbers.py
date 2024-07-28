Number=int(input("Enter range"))
l=[]
for i in range(2,Number+1):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            l.append(i)
flag=0
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if(l[i]+l[j]==Number):
            flag=1
            print(l[i],"+",l[j],"=",Number)
if(flag==0):
    print("no such combination")