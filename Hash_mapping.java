//Removing duplicate values without changing the order
//language - java using hashmap and array
import java.util.ArrayList;
import java.util.HashMap;
public class Hash_mapping {
    public static void main(String[] args) {
        ArrayList<Integer> retarr = new ArrayList<>();
        int[] arr = {1,2,3,4,5,6,7,7,10,10,19,19};
        HashMap<Integer,Integer> Map = new HashMap<>();
        int i=0;
        int len = arr.length;
        for(i=0;i<len;i++){
            if(Map.containsValue(arr[i])){
            }
            else {
                Map.put(i,arr[i]);
                retarr.add(arr[i]);
            }
        }
        System.out.println(retarr);
    }
}
