```java
import java.util.* ;
class HelloWorld {
    public static void main(String[] args) {
        int[] arr ={ 2 , 7 , 11 , 15 } ;
        int target = 9 ;
        int[] result = targetindex(arr , target) ;
     System.out.print(Arrays.toString(result)) ;
    } 
     public static int[] targetindex( int[] arr , int target ){
        for ( int i = 0 ; i < arr.length ; i++){
            for ( int j= i+ 1 ; j < arr.length ; j++){
                if ( arr[i] + arr[j] == target){
                    return new int[] {i , j} ;
                }
            }
        }
    return null ;
        
    }
}
```
