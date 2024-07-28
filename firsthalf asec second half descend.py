l=[10,100,90,50,60,30,40,70]
l.sort()
tempascen=[]
tempdesc=[]
n=len(l)
for i in range(0,n//2):
    tempascen.append(l[i])
for i in range(n//2,n):
    tempdesc.append(l[i])
tempascen.sort()
tempdesc.sort(reverse=True)
l=tempascen+tempdesc
print(l)