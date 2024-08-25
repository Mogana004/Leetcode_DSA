[7)remove Spaces](https://www.geeksforgeeks.org/problems/remove-spaces0128/1)

S = "geeks  for geeks"

Output: geeksforgeeks

To remove all spaces from a string in Java, you can use the replace() or replaceAll() method. Both methods can replace spaces with an empty string, effectively removing them.

```java
class Solution
{
   
    String modify(String S)
    {
        S = S.trim() ;
       String removespace = S.replaceAll(" " , "");
       return removespace ;
       
    }
}
```
