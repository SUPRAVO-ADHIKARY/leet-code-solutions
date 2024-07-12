public class randommissing {
    public static int missingNumber(int arr[],int n){
        int originalSum =((n+1)*(n+2))/2;
        int newSum=0;
        for (int i=0;i<n;i++){
            newSum=newSum+arr[i];
        }
        return (originalSum - newSum);
    }

    public static void main(String[] args) {
        int arr[]= {1,2,3,4,5,7,8,9,10};
        int n = arr.length;
        System.out.println("your missing number is "+missingNumber(arr,n));
    }
}
