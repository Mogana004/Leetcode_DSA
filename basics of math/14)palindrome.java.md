```java
class Solution {
    public boolean isPalindrome(int x) {
        int original = x;
        if (x < 0) {
            return false;
        }
        int reverse = 0 ;
        while (x != 0 ){
            int digit = x % 10 ;
            reverse = 10 * reverse + digit ;

            x= x / 10 ;
        }
        return reverse == original;

    }
}
```
![image](https://github.com/Mogana004/Leetcode_DSA/assets/92911280/4cc7a916-e4b8-42a0-8585-8b444d78414e)

