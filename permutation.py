N=int(input("enter N"))
R=int(input("enter R"))
numerator=1
denominator=1
if(N==1 or N==0):
    print(1)
temp=N
while(N>=1):
    numerator=numerator*N
    N=N-1
N=temp-R
while(N>=1):
    denominator=denominator*N
    N=N-1
print(numerator//denominator)