# median 
#### logic 
1) if array size is odd  - return middle value
2) if  even - calculate - sum( mid + (mid -1 ) ) /2  

```java

class Solution
{
    public int find_median(int[] v)
    {
        Arrays.sort(v) ;
        int n = v.length ;
        
        int mid_index = n /2 ;
        int sum = 0 ;
        for ( int i =0 ; i < n ; i++){
           
        
            
            if (n % 2 == 0 ){
                
                sum = sum + (v[mid_index] + v[mid_index - 1] );
                int avg = sum / 2;
               
                return (int) avg ;
            }
            else{
                return v[mid_index] ;
            }
            
        }
        return -1 ;
    }
}
```
# mean 
```java
class Solution {
    static int mean(int N , int[] A) {
       int sum = 0 ;
       for ( int i = 0 ; i < N ; i++){
           sum = sum + A[i] ;
           
       }
       int mean = sum / N ;
       return (int)mean ;
    }
};
```
