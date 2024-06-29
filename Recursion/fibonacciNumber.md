![image](https://github.com/Mogana004/Leetcode_DSA/assets/92911280/c41297d2-a3c1-4057-a4c5-f7f10b08808f)
# code 
```java
class Solution {
    public int fib(int n) {
        if (n==0 ){
            return 0 ;
        }
        else if (n==1){
            return 1 ;
        }
        int fibonacci = fib(n-1) + fib(n-2) ;
        return fibonacci ;
    }
}
```
