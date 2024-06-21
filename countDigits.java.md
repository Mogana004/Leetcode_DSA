![image](https://github.com/Mogana004/Leetcode_DSA/assets/92911280/9fd98783-3d3e-4bbe-b933-53b88ecb3216)

```java
class Solution{
    static int evenlyDivides(int N){
        int count = 0 ;
        int originaln = N ;
        while ( N != 0 ){
            int digit = N % 10 ;
            if ( digit != 0 && originaln % digit == 0) {
                count++ ; 
            }
           
            N = N / 10 ;
            
        }
        return count ;
        
        
    }
}
```
