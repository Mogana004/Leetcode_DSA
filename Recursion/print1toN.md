![image](https://github.com/Mogana004/Leetcode_DSA/assets/92911280/ec1f6ee6-dab8-4a27-92ad-2d177a124322)
# code
```java
import java.util.Scanner;

class Solution {
   
    static void print(int n, int stop) {
        // The base case should check if n >= stop to stop the recursion
        if (n >= stop) {
            return;
        }
        // Print the current number
        System.out.print(n + " ");
        // Recursive call to print the next number
        print(n + 1, stop);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the stopping number: ");
        int stop = sc.nextInt(); 
        int n = 1; // Starting number
        
        print(n, stop); 
    }
}
```
