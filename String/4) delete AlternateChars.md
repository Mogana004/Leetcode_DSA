4) [delete AlternateChars](https://www.geeksforgeeks.org/problems/java-delete-alternate-characters4036/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card)
```java
class Solution {
    static String delAlternate(String S) {
        StringBuffer result = new StringBuffer() ;
        for ( int i= 0 ; i < S.length() ; i++){
            if ( i %2 == 0 ){
                result.append(S.charAt(i));
                
               
            }
        }
        return result.toString() ;
    }
}
```
