A=[1,2,3]
B=[1,2,3,4,5]
C=[]
l1=len(A)
l2=len(B)
if(l1>l2):
    maxl=l1
else:
    maxl=l2
for i in range(0,maxl):
    if(A[i] in B[i] and B[i] in A[i]):
        C.append(A[i])
    else:
        C.append(A[i])
        C.append(B[i])
print(C)