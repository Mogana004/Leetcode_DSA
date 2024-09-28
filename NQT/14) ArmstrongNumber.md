```java
class Solution {
    static String armstrongNumber(int n) {
        double sum = 0 ;
        int original = n ;
        while ( n > 0){
            int digit = n % 10 ;
            sum = sum + Math.pow(digit , 3 ) ; 
            n = n /10  ;
        }
       if ( sum == original){
           return "true" ;
       }
       return "false" ;
    }
}
```
