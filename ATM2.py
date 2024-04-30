t=int(input())
for i in range(1,t+1):
    N,K=map(int,input().split())
    L=list(map(int,input().split()))
    for i in range(1,N+1):
        withdraw=L[i-1]
        if(K-withdraw>=0):
            print(1,end='')
            K=K-withdraw
        else:
            print(0,end='')
    print("\n")
