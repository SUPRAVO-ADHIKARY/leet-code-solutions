l=[80,20,30,40,50,60,70,80,90]
max=l[0]
min=l[0]
for i in range(0,len(l)):
    if(l[i]>max):
        max=l[i]
    if(l[i]<min):
        min=l[i]
print("max",max)
print("min",min)