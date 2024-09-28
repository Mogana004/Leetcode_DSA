```java
class Solution {
    public int maximumProduct(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length ;
        int product1 = nums[n-1] * nums[n-2] * nums[n-3] ;
        int product2 = nums[0] * nums[1] * nums[n-1] ;
        if ( product1 > product2){
            return product1 ;
        }
        else{
            return product2 ;
        }
    }
}
```
![image](https://github.com/user-attachments/assets/ad265039-09ff-43bc-92e5-c2f8478241b0)
