
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
# -------------------------------------------------------------------------------------------------------
# GCD Calculation:

The gcd method calculates the GCD of two numbers using the Euclidean algorithm. This method repeatedly sets a to b and b to a % b until b becomes 0. The GCD is then the last non-zero value of a.
## Formula 
### ( b , a% b )
#  -------------------------------------------------------------------------------------------------------

# LCM Calculation:

The LCM is calculated using the formula:
Product of two numbers = ( LCM * GCD ) 
### therefore , LCM = Product of numbers / GCD 
#  -------------------------------------------------------------------------------------------------------

![image](https://github.com/Mogana004/Leetcode_DSA/assets/92911280/f444b4fc-24df-4119-b4df-e46ea030707b)
