## without using an additional array. 

This method uses a two-pass approach to first count the zeros and then rearrange the array
### Explanation:
#### 1) Count Zeros: We first count the number of zeros in the array.
#### 2) Shift Non-Zero Elements: We iterate from the end of the array to the beginning. For each non-zero element, we place it at the current position indicated by index, and then decrement index. This effectively shifts all non-zero elements to the end while maintaining their relative order.
#### 3) Fill Zeros: We fill the beginning of the array with the counted number of zeros.
#### 4) Print the Result: Finally, we print the modified array.
```java
import java.util.*;

class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int array[] = new int[n];
        
        for (int i = 0; i < n; i++) {
            array[i] = sc.nextInt();
        }
        
        // Count the number of zeros
        int zeroCount = 0;
        for (int i = 0; i < n; i++) {
            if (array[i] == 0) {
                zeroCount++;
            }
        }
        
        // Shift non-zero elements to the right positions
        int index = n - 1;
        for (int i = n - 1; i >= 0; i--) {
            if (array[i] != 0) {
                array[index] = array[i];
                index--;
            }
        }
        
        // Fill the beginning of the array with zeros
        for (int i = 0; i < zeroCount; i++) {
            array[i] = 0;
        }
        
        // Print the result array
        for (int i = 0; i < n; i++) {
            System.out.print(array[i] + " ");
        }
    }
}
```



## 2nd approach  -using an extra array 
```java
import java.util.*;

class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int array[] = new int[n];
        
        for (int i = 0; i < n; i++) {
            array[i] = sc.nextInt();
        }
        
        // Count the number of zeros
        int zeroCount = 0;
        for (int i = 0; i < n; i++) {
            if (array[i] == 0) {
                zeroCount++;
            }
        }
        
        // Create a new array to hold the result
        int[] result = new int[n];
        
        // Fill the front of the result array with zeros
        for (int i = 0; i < zeroCount; i++) {
            result[i] = 0;
        }
        
        // Fill the rest of the result array with non-zero elements in original order
        int index = zeroCount;
        for (int i = 0; i < n; i++) {
            if (array[i] != 0) {
                result[index] = array[i];
                index++;
            }
        }
        
        // Print the result array
        for (int i = 0; i < n; i++) {
            System.out.print(result[i] + " ");
        }
    }
}
```

