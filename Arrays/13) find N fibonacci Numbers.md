### complete printFibb() which takes single argument N and returns a list of first N Fibonacci numbers.
![image](https://github.com/user-attachments/assets/eafd3712-929a-4e20-aa63-0a9aa5de114e)

```java
class Solution {
    // Function to return list containing first n Fibonacci numbers.
    public static long[] printFibb(int n) {
        if (n <= 0) {
            return new long[0];
        }

        long[] fibNumbers = new long[n];

        if (n >= 1) {
            fibNumbers[0] = 1;
        }
        if (n >= 2) {
            fibNumbers[1] = 1;
        }

        for (int i = 2; i < n; i++) {
            fibNumbers[i] = fibNumbers[i - 1] + fibNumbers[i - 2];
        }

        return fibNumbers;
    }
}
```
