
## Remove dupe and return coutn of unique elements  
```java
import java.util.*;

class Solution {
  public static void main(String[] args) {
      Scanner sc = new Scanner(System.in) ;
      int n = sc.nextInt() ;
    int arr[] = new int[n] ; 
    for ( int i = 0 ; i < n ; i++){
        arr[i] = sc.nextInt() ;
    }
    
    int j = 0 ;
    for ( int i = 1 ; i <= n-1 ; i++){
        if ( arr[j] != arr[i] ){
            arr[j+1 ] = arr[i] ;
            j++ ;
        }
    }
    System.out.println(j+1) ;
    
    for ( int  i= 0 ; i < n ; i++) {
        System.out.print(arr[i] + " ") ;
    }
  }
}
```
![image](https://github.com/user-attachments/assets/fec7ee10-4bde-4d9f-8902-3bac7f863759)
