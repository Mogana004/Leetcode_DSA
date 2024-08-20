## [Array Duplicates](https://www.geeksforgeeks.org/problems/find-duplicates-in-an-array/1?page=1&difficulty=Easy&sortBy=submissions)
Input: n = 5, arr[] = [2,3,1,2,3]

Output: 2 3 

Explanation: 2 and 3 occur more than once in the given array.

```java
class Solution {
    public static ArrayList<Integer> duplicates(int[] arr) {
        int n = arr.length;
        ArrayList<Integer> dupe = new ArrayList<>();
        
       for ( int i = 0 ; i < n ; i++) {
           int count = 0 ;
           for (int j= 0 ; j < n ; j++){
               if ( arr[i] == arr[j]){
                   count++ ;
                   
               }
           }
           if ( count > 1 && !dupe.contains(arr[i])){
               dupe.add(arr[i]);
           }
           
           
       }
        
        Collections.sort(dupe) ;
         // If no duplicates were found, return [-1]
        if (dupe.isEmpty()) {
            dupe.add(-1);
        }
        
        return dupe;
    
        
    }
}
```
