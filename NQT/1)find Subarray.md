### 1) find Subarray with sum k 
import java.util.*  ;
class HelloWorld {
    public static void main(String[] args) {
       int arr[] = {11 , 2 ,34 , 5, 4 ,69 } ;
       int n = arr.length ;
       int target = 9  ;
       for ( int i = 0 ; i < n ; i++){
           int sum = 0 ;
           for ( int j = i ; j < n ; j++){
               sum = sum + arr[j] ;
               if ( sum == target ){
                  System.out.println(Arrays.toString(Arrays.copyOfRange(arr, i, j + 1)));
               }
           }
       }
        
    }
}
