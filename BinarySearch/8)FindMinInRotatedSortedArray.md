#  [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)

### Example 
 arr = [4,5,6,7,0,1,2,3]
Result:
 0
Explanation:
 Here, the element 0 is the minimum element in the array.

### Algorithm 
1) Place the 2 pointers i.e. low and high .
2) Calculate the ‘mid.
3) Identify the sorted half, and after picking the leftmost element, eliminate that half. If arr[low] <= arr[mid] .
4) Otherwise, if the right half is sorted: min(ans, arr[mid])

```java
class Solution {
    public int findMin(int[] nums) {
        int n = nums.length;
        int low = 0;
        int high = n - 1;
        int ans = Integer.MAX_VALUE;

        while (low <= high) {
            int mid = (low + high) / 2;

            // If the left half is sorted
            if (nums[low] <= nums[mid]) {
                // Take the minimum of the current answer and the leftmost element
                ans = Math.min(ans, nums[low]);
                // Eliminate the left half
                low = mid + 1;
            } else {
                // Otherwise, take the minimum of the current answer and the middle element
                ans = Math.min(ans, nums[mid]);
                // Eliminate the right half
                high = mid - 1;
            }
        }
        return ans;
    }
}
```
