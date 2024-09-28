  ```java
class Solution {
    public boolean isHappy(int n) {
        while (n != 1 && n != 4 ) {  // '4' is used here because all non-happy numbers eventually fall into a cycle that includes 4
            n = getSumOfSquare(n);
        }
        return  n== 1 ;
    }

    public int getSumOfSquare(int n) {
        int sum = 0;
        while (n > 0) {
            int digit = n % 10;
            sum += digit * digit;
            n /= 10;
        }
        return sum;
    }
}
```
