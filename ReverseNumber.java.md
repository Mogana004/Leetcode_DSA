![image](https://github.com/Mogana004/Leetcode_DSA/assets/92911280/81d39d96-e4e7-483f-99dc-2df373eecd3a)
```java

class Solution {
    public int reverse(int x) {
        int num = x;
        long rev = 0;
        while(num != 0){
            int digit = num%10;
            rev = 10*rev + digit;
            if(rev > Integer.MAX_VALUE)return 0;
            if(rev < Integer.MIN_VALUE)return 0;
            num/=10;
        }
        return (int)rev;
    }
}
```
