Input: arr[] = [2, 4, 1, 3, 5]

Output: 3

Explanation: The third largest element in the array [2, 4, 1, 3, 5] is 3.

```java
class Solution {
    int thirdLargest(int arr[]) {
        int first = Integer.MIN_VALUE ;
        int second = Integer.MIN_VALUE ;
        int third =Integer.MIN_VALUE ;
        
        for ( int i =0 ; i < arr.length ; i++){
            if ( arr[i] > first ){
                third = second ;
                second = first ;
                first = arr[i] ;
                
            }
            /* If arr[i] is in between first and
            second then update second  */
            else if (arr[i] > second) {
                third = second;
                second = arr[i];
            }

            else if (arr[i] > third)
                third = arr[i];
        
        }
        return third ;
    }
}
```
