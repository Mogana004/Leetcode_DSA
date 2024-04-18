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
