## 11 ) valid paranthesis [leetcode](https://leetcode.com/problems/remove-outermost-parentheses/)
#### Approach
To solve this problem, you can use a stack or a counter to keep track of the depth of the parentheses. However, a counter is more efficient in this case.
```java
class Solution {
    public String removeOuterParentheses(String s) {
        StringBuilder sb = new StringBuilder();
        int depth = 0;
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            
            if (c == '(') {
                if (depth > 0) {
                    sb.append(c);
                }
                depth++;
            } else if (c == ')') {
                depth--;
                if (depth > 0) {
                    sb.append(c);
                }
            }
        }
        
        return sb.toString();
    }
}
```
