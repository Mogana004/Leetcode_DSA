## longestSubarray With Sum K
![image](https://github.com/user-attachments/assets/ddaf2bea-2637-488e-a8fd-52bbd549cdb2)

```java
import java.util.*;

class Solution {
  public static void main(String[] args) {
      Scanner sc = new Scanner(System.in) ;
     int n = sc.nextInt() ;
     int k = sc.nextInt() ;
     
      int[] arr = new int[n] ;
      for ( int i = 0 ; i< n ; i++){
          arr[i] = sc.nextInt() ;
          
      }
      int max = 0 ;
      
      for( int i = 0 ; i < n ; i++){
          int sum = 0 ;
          for ( int j = i ; j < n ; j++){
              sum += arr[j] ;
              int len = j-i + 1 ;
              if ( sum == k ) {
                  if( len > max){
                      max = len ;
                      
                  }
              }
          }
         
      }
       System.out.print(max );
  }
}
```
