## 6) Remove Vowels

Input: S = "welcome to geeksforgeeks"

Output: wlcm t gksfrgks

```java

class Solution {
    String removeVowels(String S) {
        StringBuffer sb = new StringBuffer() ;
        for ( int i = 0 ; i < S.length() ; i++){
             char ch = S.charAt(i) ;
            ch = Character.toLowerCase(ch) ;
            if ( ch != 'a' && ch !='e' && ch !='i' && ch != 'o' && ch !='u'){
                sb.append(ch) ;
            }
        }
        return sb.toString() ;
    }
}
```
