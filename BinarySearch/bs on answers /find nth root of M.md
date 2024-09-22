```java
import java.util.*;

class Solution {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    
    // Input n and m
    int n = sc.nextInt();  // The degree of the root
    long m = sc.nextLong();  // The number for which we want to find the nth root
    
    // Find and print the nth root of m
    System.out.println(findRoot(n, m));
  }
  
  // Function to find the integer nth root of m using binary search
  public static long findRoot(int n, long m) {
    long low = 1;
    long high = m;
    
    while (low <= high) {
      long mid = low + (high - low) / 2;
      
      // Calculate mid^n
      long midPower = power(mid, n);
      
      // Check if mid^n is equal to m
      if (midPower == m) {
        return mid;  // Return mid as the nth root of m
      }
      else if (midPower > m || midPower < 0) {  // Handle overflow by checking if midPower is negative
        high = mid - 1;  // If mid^n is too large, search the left half
      }
      else {
        low = mid + 1;  // If mid^n is too small, search the right half
      }
    }
    
    return -1;  // If no integer nth root is found, return -1
  }
  
  // Helper function to calculate base^exponent
  public static long power(long base, int exponent) {
    long result = 1;
    
    for (int i = 0; i < exponent; i++) {
      result *= base;
      if (result < 0) {  // Check for overflow
        return Long.MAX_VALUE;
      }
    }
    
    return result;
  }

```
