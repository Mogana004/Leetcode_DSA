```java
class Solution 
{ 
    int findLength(String s) 
    {  s= s.trim() ; 
       String split[] = s.split(" ");
       int len = split.length ;
       String lastword = split[len - 1] ; //to get the last word 
       
        int lengthOfLastWord = lastword.length();
          return   lengthOfLastWord ;
    }
  
}
```
### Explanation:
1) Trimming the String:

input.trim(); removes any leading or trailing spaces, ensuring that you don’t get an empty last word due to trailing spaces.
Splitting the String:

2) input.split(" "); splits the string into an array of words based on spaces.
Accessing the Last Word:

3) words[words.length - 1]; gets the last word in the array.


4) Finding the Length:

lastWord.length(); calculates the length of the last word.


### Example:
Input: "Hello World "
Output: 5 (since the last word is "World" and its length is 5)
