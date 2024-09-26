### 258. Add Digits

Hint
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38

Output: 2

Explanation: The process is

38 --> 3 + 8 --> 11

11 --> 1 + 1 --> 2 

Since 2 has only one digit, return it.



```java
class Solution {
    public int addDigits(int num) {
        // Continue summing digits until the result is a single digit
        while (num >= 10) {
            int sum = 0;
            while (num > 0) {
                sum += num % 10;  // Add the last digit to the sum
                num /= 10;         // Remove the last digit
            }
            num = sum;             // Set num to the sum of its digits
        }
        return num;  // Return the final single digit result
    }
}
```
