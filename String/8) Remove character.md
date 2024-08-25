8) [remove characters](https://www.geeksforgeeks.org/problems/remove-character3815/1)
```java
class Solution{
    static String removeChars(String string1, String string2){
        StringBuffer sb = new StringBuffer(string1) ;
        int len = string2.length() ;
        for ( int i = 0 ; i < len ; i++){
            char ch = string2.charAt(i);
             for (int j = 0; j < sb.length(); j++) {
                if (sb.charAt(j) == ch) {
                    sb.deleteCharAt(j);
                    j--; // Move index back by 1 as length reduces
                }
            }
        }
        
        return sb.toString();
    }
}
```

## Explanation:
1) StringBuffer Initialization:
 We initialize StringBuffer with string1 because StringBuffer is mutable and allows for efficient string manipulation.
2) Nested Loops:
Outer loop iterates over each character in string2.
Inner loop iterates over the StringBuffer to find and remove occurrences of the current character from string2.
3) Character Removal:
sb.deleteCharAt(j) removes the character at the specified index j. We then decrement j to ensure we don't skip the next character due to the reduced length of StringBuffer.
