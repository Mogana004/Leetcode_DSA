![image](https://github.com/Mogana004/Leetcode_DSA/assets/92911280/2f0a5623-9abe-4082-bd82-7008ef4c3b31)
```java
class Solution {
    public int removeElement(int[] nums, int val) {
        int pointer = 0;
        for (int i=0 ; i< nums.length ; i++){
            if (nums[i] != val){
                nums[pointer] = nums[i];
                pointer++;
            }
        }
        return pointer;
    }
}
```
## Explanation :
#### * The approach used here is similar to the two-pointer technique.
#### * We initialize a pointer (pointer) to keep track of the position where we should place elements without the value "val".
#### * We iterate through the array using a loop.
#### * If we encounter an element that is not equal to val, we copy that element to the position indicated by the pointer and then increment the pointer.
#### * Essentially, we keep track of the position where valid elements are to be placed, effectively removing the elements with the value "val".
