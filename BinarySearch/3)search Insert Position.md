# 35. Search Insert Position
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

## example 
Input: nums = [1,3,5,6], target = 5
Output: 2

## code 
```java
class Solution {
    public int searchInsert(int[] nums, int target) {
        int n = nums.length ;
        int low = 0 ;
        int high = n- 1 ;
        int ans = n ;

        while ( low <= high){
            int mid = (low + high ) / 2 ;
            if ( nums[mid] >= target ){
                ans = mid ;
                high = mid - 1 ;


            }
            else{
                low = mid + 1 ;
            }
        }
        return ans ;
    }
}
```
