
```java
class Solution {
    static Long[] lcmAndGcd(Long A , Long B) {
         Long gcd = gcd(A, B);
        
        // Calculate LCM using the relationship LCM(A, B) = (A * B) / GCD(A, B)
        Long lcm = (A * B) / gcd;
        
        // Return the results in a Long array
        return new Long[] { lcm, gcd };
    }

    // Helper method to calculate GCD using the Euclidean algorithm
    private static Long gcd(Long a, Long b) {
        while (b != 0) {
            Long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
    }
```
![image](https://github.com/Mogana004/Leetcode_DSA/assets/92911280/f444b4fc-24df-4119-b4df-e46ea030707b)
