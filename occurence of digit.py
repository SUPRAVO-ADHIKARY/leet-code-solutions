N=int(input("enter the number"))
dig=int(input("enter the digit"))
count=0
while(N>0):
    rem=N%10
    if(rem==dig):
        count+=1
    N=N//10
print(count)
