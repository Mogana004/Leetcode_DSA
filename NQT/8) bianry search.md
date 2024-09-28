```java
class Javaprogram {
    public static void main(String[] args) {
        int arr[] = {1, 2, 3, 9, 5, 8};  // The array should be sorted for binary search
        int target = 5;
        System.out.println(binarysearch(arr, target));
    }

    public static int binarysearch(int[] arr, int target) {
        int low = 0;
        int high = arr.length - 1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;  // Corrected mid calculation
            
            if (arr[mid] == target) {
                return mid;
            } else if (arr[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        
        return -1;  // Target not found
    }
}
```
