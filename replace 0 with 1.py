N=int(input("Enter the integer"))
l=[]
while(N>0):
    rem=N%10
    if(rem==0):
        l.append(1)
    else:
        l.append(rem)
    N=N//10
for i in range(len(l)-1,-1,-1):
    print(l[i],end="")