### 1) string Concatination 
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Initialize two strings
        String s1 = "Mogana";
        String s2 = "Varshini";
        
        // Concatenate the strings
        String s3 = s1.concat(s2);
        
        // Print the concatenated string
        System.out.println("The concatenated String is: " + s3);
    }
}
```
### 2) find length of strings

C:\Users\ACER\Documents>java Main
enter string 1 :
Mogana
6
enter string 2 :
MuthuKumar
10
C:\Users\ACER\Documents>

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Create a Scanner object for user input
        Scanner sc = new Scanner(System.in);
        
        // Read the first string
        System.out.println("Enter string 1:");
        String s1 = sc.nextLine();
        // Print the length of the first string
        System.out.println("Length of string 1: " + s1.length());
        
        // Read the second string
        System.out.println("Enter string 2:");
        String s2 = sc.nextLine();
        // Print the length of the second string
        System.out.println("Length of string 2: " + s2.length());
        
        // Close the scanner
        sc.close();
    }
}
```

### 3) Reverse string (https://www.geeksforgeeks.org/problems/reverse-a-string/1)[GFG]
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter string 1:");
        String s1 = sc.nextLine();
        
        // Initialize an empty string for the reversed string
        String rev = "";
        
        // Loop through the string from the end to the beginning
        for (int i = s1.length() - 1; i >= 0; i--) {
            rev = rev + s1.charAt(i); 
        }
        
        // Print the original and reversed strings
        System.out.println("Original string: " + s1);
        System.out.println("Reversed string: " + rev);
        
      
        sc.close();
    }
}
```
