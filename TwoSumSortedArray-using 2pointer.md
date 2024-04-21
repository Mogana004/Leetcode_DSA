![image](https://github.com/Mogana004/Leetcode_DSA/assets/92911280/65d31c68-8f53-490c-b330-0ce568c3e9f5)

```java
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int pointer_1 = 0;
        int pointer_2 = numbers.length - 1;
        
        while (pointer_1 < pointer_2) {
            int sum = numbers[pointer_1] + numbers[pointer_2]; // Calculate the sum only once
            
            if (sum == target) {
                return new int[]{pointer_1 + 1, pointer_2 + 1};
            } else if (sum < target) {
                pointer_1++; // Increment pointer_1 since the sum is too small
            } else {
                pointer_2--; // Decrement pointer_2 since the sum is too large
            }
        }
        return new int[0];
    }
}
```

## explanation 
#### The method used to solve the "Two Sum II - Input array is sorted" problem involves employing the two-pointer technique. Here's how it works:

##### Initialize Pointers: Start by initializing two pointers, usually named left and right, pointing to the beginning and the end of the sorted array, respectively.
##### Iterate Until Pointers Meet: Use a loop to iterate until the left pointer is less than or equal to the right pointer. This condition ensures that the pointers do not cross each other.
##### Check Sum: At each iteration, calculate the sum of the elements pointed to by the left and right pointers.
### Adjust Pointers Based on Sum: Depending on the sum calculated:
1) If the sum equals the target, return the indices of the elements pointed to by the left and right pointers.
2) If the sum is less than the target, increment the left pointer to move towards larger values.
3) If the sum is greater than the target, decrement the right pointer to move towards smaller values.
4) Repeat Until Solution Found or Pointers Meet: Continue this process until either a pair with the target sum is found, in which case return the indices, or until the pointers meet, indicating that no such pair exists.

 
