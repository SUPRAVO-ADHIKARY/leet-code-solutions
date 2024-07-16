public class fisrtandlastoccurence {
    static void firstAndLastOccurence(int arr[],int target){
        int first=-1,last=-1;
        for(int i=0;i<arr.length;i++){
            if(arr[i]==target && first==-1){
                first=i;
            }
            if(arr[i]==target && first!=-1){
                last=i;
            }
        }
        if(first!=-1 && last==-1){
            last=first;
            System.out.println(first+" "+last);
        }
        else {
            System.out.println(first+" "+last);
        }
    }

    public static void main(String[] args) {
        int arr[]={1,1,2,2,3,4,2};
        int target=5;
        firstAndLastOccurence(arr,target);
    }
}
