## code solution - 66. plus one 
```java
class Solution {
    public int[] plusOne(int[] digits) {
          // Traverse the array from the end
          int n = digits.length;
        for (int i = n - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }

        // If all digits are 9, we need an extra digit
        int[] newDigits = new int[n + 1];
        newDigits[0] = 1;
        return newDigits;
    
    }
}
```

## explanation 
If Input = [1, 2, 3]
i = 2
digits[2] = 3
Since digits[2] is less than 9, increment it by 1 and return the array.

digits[2]++;  // digits = {1, 2, 4}
return digits;  // Return {1, 2, 4}


## leetcode problem 
![image](https://github.com/user-attachments/assets/8d7bb408-2d9e-49b6-98ab-431f1a0be38b)
