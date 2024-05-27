import math 
num=int(input("enter number"))
sum=0
last=0
i=0
while(num>0):
    last=num%10
    sum=sum+last*(math.pow(2,i))
    i=i+1
    num=num//10
print(int(sum))