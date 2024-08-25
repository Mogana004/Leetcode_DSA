### Sum of numbers in string [GFG](https://www.geeksforgeeks.org/problems/sum-of-numbers-in-string-1587115621/1)

```java

class Solution {
    // Function to calculate sum of all numbers present in a string.
    public static long findSum(String str) {
        long sum = 0;
        int num = 0;
        
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            
            // Check if the character is a digit
            if (ch >= '0' && ch <= '9') {
                // Convert the character to its corresponding numeric value
                num = num * 10 + (ch - '0');
            } else {
                // If the character is not a digit, add the current number to the sum and reset num
                sum += num;
                num = 0;
            }
        }
        
        // Add the last number found in the string
        sum += num;
        
        return sum;
    }
}
```

## explanation 
1) subtracting '0' from any digit character gives you the actual numeric value of that character.
2) First Iteration (ch = '1'):

 num = num * 10 + (ch - '0')
 num = 0 * 10 + ('1' - '0')
 num = 0 + 1
 num = 1

Second Iteration (ch = '2'):

 num = num * 10 + (ch - '0')
 num = 1 * 10 + ('2' - '0')
 num = 10 + 2
 num = 12

### example 

str = 1abc23

Output: 24
