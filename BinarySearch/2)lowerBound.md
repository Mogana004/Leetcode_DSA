## Optimal Approach (Using Binary Search): 
As the array is sorted, we will apply the Binary Search algorithm to find the index. The steps are as follows:

We will declare the 2 pointers and an ‘ans’ variable initialized to n i.e. the size of the array(as If we don’t find any index, we will return n).

### Place the 2 pointers i.e. low and high: Initially, we will place the pointers like this: low will point to the first index, and high will point to the last index.
### Calculate the ‘mid’: Now, we will calculate the value of mid using the following formula:
#### mid = (low+high) // 2 
Compare arr[mid] with x: With comparing arr[mid] to x, we can observe 2 different cases:
#### Case 1 - If arr[mid] >= x: This condition means that the index mid may be an answer. So, we will update the ‘ans’ variable with mid and search in the left half if there is any smaller index that satisfies the same condition. Here, we are eliminating the right half.
#### Case 2 - If arr[mid] < x: In this case, mid cannot be our answer and we need to find some bigger element. So, we will eliminate the left half and search in the right half for the answer.


```java
public class Solution {
    public static int lowerBound(int []arr, int n, int x) {
       int low = 0 ;
       int high = n -1 ;
       int ans = n ;
       while ( low <= high ){
           int mid = ( low + high ) / 2 ;
           if ( arr[mid] >= x){
               ans = mid ;
               high = mid - 1 ;

           }
           else{
               low = mid + 1 ;

           }
       }
       return ans ;

    }
    public static void main(String[] args) {
        int[] arr = {3, 5, 8, 15, 19};
        int n = 5, x = 9;
        int ind = lowerBound(arr, n, x);
        System.out.println("The lower bound is the index: " + ind);
    }
}
```
