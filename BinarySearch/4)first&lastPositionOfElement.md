# [first & last Position Of Element](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) 

### Example 1:
### Input: N = 7, target=13, array[] = {3,4,13,13,13,20,40}
### Output: 4
### Explanation: As the target value is 13 , it appears for the first time at index number 2.

## Naive approach 
```java
class Solution {
    public int[] searchRange(int[] nums, int target) {
        int first = -1 ;
        int last = -1 ;
        for ( int i = 0 ; i <nums.length ; i++){
            if ( nums[i] == target ){
                if ( first == -1){
                   first = i;
                }
                last = i; // Always update last when we find the target
            }
        }
        return new int[]{first, last};
    }
}

```
