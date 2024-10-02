```java
class Solution {
    public boolean isAnagram(String s, String t) {
        // Normalize by removing spaces
        String change1 = s.replaceAll("\\s+", "");
        String change2 = t.replaceAll("\\s+", ""); // Fixed 't' instead of 's'

        // Convert to char arrays
        char[] charArray1 = change1.toCharArray();
        char[] charArray2 = change2.toCharArray();

        // Sort the arrays
        Arrays.sort(charArray1);
        Arrays.sort(charArray2);

        // Compare the sorted arrays
        return Arrays.equals(charArray1, charArray2);
    }
}
```
