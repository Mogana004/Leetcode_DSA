## 5) palindromeStrings

note:
1) we must use the .equals() method to compare the strings instead of "==" .
2)  convert the string to an mutable sequence using the string builder class and reverse the string using .reverse() method .
3)  then convert the stringBuffer object back to String and return 1 if palindrome else return 0 . 

```java

class Solution {
    int isPalindrome(String S) {
        StringBuffer sb = new StringBuffer(S) ;
        String reverse = sb.reverse().toString() ;
        if ( S.equals(reverse)){
            return 1 ;
        }
        else{
            return 0 ;
        }
    }
};
```
