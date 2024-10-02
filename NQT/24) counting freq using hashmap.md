```java
import java.util.* ;

class Practice {
    public static void main(String[] args) {
        int[] arr = new int[5]; 
        HashMap<Integer, Integer> hm = new HashMap<>(); 
        Scanner sc = new Scanner(System.in);

        // Input the array values
        System.out.println("Enter 5 integers:");
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }

        // Count the frequency of each element
        for (int i = 0; i < arr.length; i++) {
            if (hm.containsKey(arr[i])) {
                hm.put(arr[i], hm.get(arr[i]) + 1); // Increment the frequency
            } else {
                hm.put(arr[i], 1); // First occurrence, set count to 1
            }
        }

        // Print the frequency map
        System.out.println(hm);
    }
}
```
