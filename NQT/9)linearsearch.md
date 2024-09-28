```java
class Javaprogram {
    public static void main(String[] args) {
        int arr[] = {1, 2, 3, 9, 5, 8};
        int target = 5;
        System.out.println(linearSearch(arr, target));
    }

    public static int linearSearch(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) {
                return i;  // Return index if target is found
            }
        }
        return -1;  // Return -1 if target is not found
    }
}
```
