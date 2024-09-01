
## Remove dupe in an sorted array in place   
```java
class HelloWorld {
    public static void main(String[] args) {
        int arr[] = {1, 1, 2, 2, 3, 4, 4, 5};
        int length = removeDuplicates(arr);
        
        // Print the array with unique elements
        for (int i = 0; i < length; i++) {
            System.out.print(arr[i] + " ");  // Output: 1 2 3 4 5 
        }
    }

    public static int removeDuplicates(int[] arr) {
        if (arr.length == 0) return 0;

        int i = 0;  // pointer for the last unique element
        
        for (int j = 1; j < arr.length; j++) {
            if (arr[i] != arr[j]) {
                i++;
                arr[i] = arr[j];
            }
        }
        return i + 1;  // The new length of the array with unique elements
    }
}

```
