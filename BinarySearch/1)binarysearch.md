### realtime example - dictionary 
## Algorithm / Intuition
We will use a couple of pointers i.e. low and high to apply binary search. Initially, the low pointer should point to the first index and the high pointer should point to the last index.
![image](https://github.com/user-attachments/assets/6c8856cc-f6b5-4866-a4bd-922218f1209c)



### Step 1: Divide the search space into 2 halves:
In order to divide the search space, we need to find the middle point of it. So, we will take a ‘mid’ pointer and do the following:
mid = (low+high) // 2 ( ‘//’ refers to integer division)
### Step 2: Compare the middle element with the target:
In this step, we can observe 3 different cases:
#### If arr[mid] == target: We have found the target. From this step, we can return the index of the target possibly.
#### If target > arr[mid]: This case signifies our target is located on the right half of the array. So, the next search space will be the right half.
#### If target < arr[mid]: This case signifies our target is located on the left half of the array. So, the next search space will be the left half.

## code 
```java
class Solution {
    public int search(int[] nums, int target) {
        int n = nums.length ;

        int low = 0 ;
        int high = n - 1 ;
        while ( low <= high ){
            int mid = (low + high ) / 2 ;

        if ( nums[mid] == target ){
            return mid ;

        }
        else if ( target > nums[mid]){
            low = mid + 1 ;
        }
        else{
            high = mid - 1 ;

        }
        
        }
        
     return -1  ;
    }
}
```
![image](https://github.com/user-attachments/assets/17239e8e-9703-4b01-8601-bb5c1a6f4478)


## similar leetcode problem - first bad version 
![image](https://github.com/user-attachments/assets/495bc7f6-3bbe-4826-ad0f-1aaf92783f8d)

