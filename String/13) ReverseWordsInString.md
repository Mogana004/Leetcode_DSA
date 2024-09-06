## ReverseWordsInString
```java
class Solution {
    public String reverseWords(String s) {
        StringBuilder rev= new StringBuilder() ; // create a stringbuilder to store the result 
        s = s.trim();
        String[] split = s.split("\\s+") ;  // 
        int len = split.length ;
        

        for ( int i= len - 1 ; i >= 0 ; i--) {
           rev.append(split[i] );
           if (i != 0) { 
                rev.append(" ");
            }

        }
  return rev.toString();
    }
}
```
