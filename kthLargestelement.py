def kLargestElement(arr,k):
    temp=[]
    l=len(arr)
    for i in range(0,l):
        temp.append(arr[i])
        temp.sort()
        if(len(temp)>k):
           temp.pop(0) 
    print("the, ",k," largest elment is ",temp[0])

arr=[10,30,40,50,90,20]
k=3
kLargestElement(arr,k)