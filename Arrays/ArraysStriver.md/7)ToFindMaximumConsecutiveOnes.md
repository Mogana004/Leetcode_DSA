## Find the number that appears once  , and the other appers twice .
```java
class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
       
        int count = 0 ;
        int maxcount = 0 ;
        
        for (int each : nums){
            if (each == 1){
                count++ ;
                maxcount = Math.max(maxcount , count);
            }
            else{
                count = 0;
            }
        }
        return maxcount;
    }

    }
```
![image](https://github.com/user-attachments/assets/89c38e62-18ef-4a6f-bd6c-d109ce596516)
 leetcode problem : https://leetcode.com/problems/single-number/

##  Note on Efficiency:
This solution has a time complexity of 
𝑂
(
𝑛
2
)
O(n 
2
 ), which is not optimal for large arrays. The optimal solution, as previously mentioned, uses the XOR approach with 
𝑂
(
𝑛
)
O(n) time complexity and 
𝑂
(
1
)
O(1) space complexity.

### For completeness, here's the optimal XOR solution again:

```java

class Solution {
    public int singleNumber(int[] nums) {
        int result = 0;
        for (int num : nums) {
            result ^= num;
        }
        return result;
    }
}
```
