```java
import java.util.*;

class Solution {
    static void bubble_sort(int[] array, int n) {
        for (int j = n - 1; j >= 1; j--) {
            for (int i = 0; i < j; i++) {
                if (array[i] > array[i + 1]) {
                    int temp = array[i];
                    array[i] = array[i + 1];
                    array[i + 1] = temp;
                }
            }
        }
    }

    public static void main(String[] args) {
        int[] array = {1, 0, 12, 8, 7, 9, 10, 5, 6, 3, 4};
        int n = array.length;

        bubble_sort(array, n);
        
        System.out.println(Arrays.toString(array));
    }
}
```
![image](https://github.com/Mogana004/Leetcode_DSA/assets/92911280/1dfd892e-0137-4767-8d0e-ac53085a1ced)
