```java
public class Solution {
    public static boolean palindromeNumber(int n){
        int original = n ;
        int reverse = 0 ;
        while ( n > 0 ){
            int d  = n % 10 ;
            reverse = (reverse * 10 ) +  d  ;
            n = n / 10 ;

        }
        if ( reverse == original ){
            return true ;
        }
        return false ;
    }
}
```
