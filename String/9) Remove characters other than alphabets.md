## Remove all characters other than alphabets[GFG](https://www.geeksforgeeks.org/problems/remove-all-characters-other-than-alphabets4923/1)
```java

class Solution{
    String removeSpecialCharacter(String s) {
       StringBuffer sb = new StringBuffer() ;
        int len = s.length() ;
        for ( int i = 0 ; i < len ; i++){
            char ch = s.charAt(i) ;
          
            if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z')) {
                sb.append(ch) ;   
            }   
        }
       // If no alphabetic characters were found, return "-1"
        if (sb.length() == 0) {
            return "-1";
        }
        
        return sb.toString();
    }
}
```
### output
-> Input: "$Gee*k;s..fo, r'Ge^eks?"
-> Output: "GeeksforGeeks" (since alphabetic characters are present)
