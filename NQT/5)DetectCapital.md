### 5) DetectCapital
![image](https://github.com/user-attachments/assets/cacc9ec8-a7af-441c-8516-2b0155d898bc)

```java
class Solution {
    public boolean detectCapitalUse(String word) {
       
        char ch = word.charAt(0);
        if ( word.equals(word.toUpperCase())){
            return true ;
        }
         if(word.equals(word.toLowerCase())){
            return true ;
         }
         if ( Character.isUpperCase(ch) && word.substring(1).equals(word.substring(1).toLowerCase())) {
            return true;
        }
        
        // If none of the conditions are met, return false
        return false;
    }
}
      
```
