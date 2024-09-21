### to fing the Suare root of a number - using Binary search 
![image](https://github.com/user-attachments/assets/4cfa206c-3e4b-472c-aadc-bc185466dcef)

```java
import java.util.Scanner;

class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int result = sqrt(n);
        
       
        System.out.println(result);
    }
    
    // Function to find the square root of N (integer square root, floor if non-perfect)
    public static int sqrt(int n) {
        // Special cases for n = 0 or 1
        if (n == 0 || n == 1) {
            return n;
        }
        
        int low = 1;
        int high = n;
        int ans = 0;
        
        // Binary search for square root
        while (low <= high) {
            int mid = low + (high - low) / 2;  
            
            // Check if mid*mid is equal to n
            if (mid * mid == n) {
                return mid;  
            }
            
            
            if (mid * mid < n) {
                low = mid + 1;
                ans = mid;  
            } else {
                
                high = mid - 1;
            }
        }
        
        
        return ans;
    }
}
```
