### Optimal Approach (Two Pointer Approach)
Approach :

1) Initialize a variable i to 0.

2) Iterate through the array, and for each non-zero element, swap it with the element at index i and increment i.


```java
import java.util.*;
public class Main {
    public static void move_zeros(int[] a, int n) {
        int i = 0;
        for (int j = 0; j <= n-1; j++) {
            if (a[j] != 0) {
                int temp = a[i];
                a[i] = a[j];
                a[j] = temp;
                i++;
            }
        }
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] a = new int[n];
        for (int i = 0; i <=n-1; i++) {
            a[i] = scanner.nextInt();
        }
        move_zeros(a, n);
        for (int i = 0; i <=n-1; i++) {
            System.out.print(a[i] + " ");
        }
    }
}
```
