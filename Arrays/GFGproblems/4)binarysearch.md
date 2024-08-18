# [binary search](https://www.geeksforgeeks.org/problems/binary-search-1587115620/1?page=1&category=Arrays&company=TCS&sortBy=difficulty)
```java
class Solution {
    public int binarysearch(int[] arr, int k) {
        int n = arr.length ;
       int low = 0 ;
       int high = n-1 ;
      while ( low <= high ){
           int mid = (low + high ) / 2;
           if ( arr[mid] == k) {
               return mid ;
           }
           else if ( arr[mid] < k){
               low = mid + 1 ;
               
           }
           else{
               high = mid - 1 ;
               
           }
       }
       return -1 ;
       
    }
}
```
