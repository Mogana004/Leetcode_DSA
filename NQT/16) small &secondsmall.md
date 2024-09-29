```java
class Solution {
    public int[] minAnd2ndMin(int arr[]) {
        int small = Integer.MAX_VALUE ;
        for ( int i = 0 ; i < arr.length ; i++){
            if ( arr[i] < small){
                small = arr[i] ;
                
            }
            
        }
        int secondsmall = Integer.MAX_VALUE;
        
         for ( int i = 0 ; i < arr.length ; i++){
             if ( arr[i] < secondsmall && arr[i] != small){
                 secondsmall = arr[i] ;
                 
             }
         }
         
         if (secondsmall == Integer.MAX_VALUE) {
            return new int[]{-1, -1}; // No second minimum found
        }
         return new int[]{small, secondsmall}; 
    }
}
```
