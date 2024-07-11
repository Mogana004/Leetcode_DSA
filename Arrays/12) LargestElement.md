```java
import java.util.*;

class Solution {
  public static void main(String[] args) {
      Scanner sc = new Scanner(System.in) ;
      int n = sc.nextInt() ;
    int[] array = new int[n];
    for (int i= 0 ; i < n ; i++) {
        array[i] = sc.nextInt() ;
    }
    
    int large = array[0] ;
    for ( int i = 0 ; i < n ; i++) {
        if ( array[i] > large){
            large = array[i] ;
        }
    }
    System.out.print(large) ;
  }
}
```
