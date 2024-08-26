## 12) remove duplicates [GFG](https://www.geeksforgeeks.org/problems/remove-all-duplicates-from-a-given-string4321/1)
```java

class Solution {
    String removeDuplicates(String str) {
        int n = str.length();
        StringBuffer sb = new StringBuffer();

        for (int i = 0; i < n; i++) {
            char ch = str.charAt(i);
            boolean found = false;

            // Check if the character is already in the result string
            for (int j = 0; j < sb.length(); j++) {
                if (sb.charAt(j) == ch) {
                    found = true;
                    break;
                }
            }

            // If the character is not found in the result, add it
            if (!found) {
                sb.append(ch);
            }
        }

        return sb.toString();
    }
}
```
