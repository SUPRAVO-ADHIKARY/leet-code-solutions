#User function Template for python3

class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        arr3=arr1+arr2
        arr3.sort()
        l=len(arr3)
        for i in range(0,l):
            if(i+1==k):
                return arr3[i]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m, k = sz[0], sz[1], sz[2]
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement( a, b, n, m, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
