# Third Max
```java
class Solution {
    public int thirdMax(int[] nums) {
        // Initialize the three max values to Long.MIN_VALUE
        long firstmax = Long.MIN_VALUE;
        long secondmax = Long.MIN_VALUE;
        long thirdmax = Long.MIN_VALUE;

        // Iterate through the array
        for (int num : nums) {
            // Skip if num is already one of the max values (to handle duplicates)
            if (num == firstmax || num == secondmax || num == thirdmax) {
                continue;
            }

            // Update first, second, and third max values
            if (num > firstmax) {
                thirdmax = secondmax;
                secondmax = firstmax;
                firstmax = num;
            } else if (num > secondmax) {
                thirdmax = secondmax;
                secondmax = num;
            } else if (num > thirdmax) {
                thirdmax = num;
            }
        }

        // If thirdmax is still Long.MIN_VALUE, it means there were fewer than 3 distinct numbers
        return (thirdmax == Long.MIN_VALUE) ? (int) firstmax : (int) thirdmax;
    }
}
```
