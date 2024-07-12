public class kadanes {
    public static long maxSubarraySum(int arr[],int n){
        long max=0;
        long sum=0;
        for(int i=0;i<n;i++){
            sum=sum+arr[i];
            if(sum<0){
                sum=0;
            }
            if(sum>max){
                max=sum;
            }
        }
        return max;
    }

    public static void main(String[] args) {
        int arr[]={1,4,5,-10,8,-6,2};
        int n=arr.length;
        System.out.println(maxSubarraySum(arr,n));
    }
}
