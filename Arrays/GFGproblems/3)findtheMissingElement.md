## [Missing in Array](https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1?page=1&category=Arrays&company=TCS&sortBy=difficulty)

The formula for the sum of the first n natural numbers is 
Sum = n×(n+1) /2
​
 .
```java
class Solution {

    // Note that the size of the array is n-1
    int missingNumber(int n, int arr[]) {
        int length = n + 1 ;
        int expectedsum = n*(n+1) /2 ;
        int actualsum =0 ;
        for ( int i = 0 ; i < n-1 ; i++){
           actualsum += arr[i] ;
           
        }
        return expectedsum - actualsum ;
    }
}
```
