```java
class Solution {
    static String armstrongNumber(int n) {
        int original = n ;
        double  sum = 0 ;
        int k = String.valueOf(n).length();
        
        
        while (n != 0 ){
            int digit = n % 10 ;
            sum = sum + Math.pow(digit , k);
            n = n / 10 ;
            
        }
        return sum == original ? "true" : "false";
        
    }
}
```
![image](https://github.com/Mogana004/Leetcode_DSA/assets/92911280/feca6f22-e21b-4868-bf5b-1bfaab27f56e)
