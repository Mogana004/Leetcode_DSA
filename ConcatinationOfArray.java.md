![image](https://github.com/Mogana004/Leetcode_DSA/assets/92911280/34704364-eb7b-4527-96d3-2d79e5e8feca)

import java.util.Arrays;

class Solution {
    public int[] getConcatenation(int[] nums) {
        int num1Len = nums.length; // Corrected declaration
        int[] ans = new int[num1Len + num1Len];
        System.arraycopy(nums, 0, ans, 0, num1Len);
        System.arraycopy(nums, 0, ans, num1Len, num1Len);
        System.out.println(Arrays.toString(ans));
        return ans; // Added return statement
    }
}
