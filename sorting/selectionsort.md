```java
import java.util.* ;
class HelloWorld {
     
   static void selection_sort(int arr[], int n) {

 // Outer loop to iterate over each element in the array (except the last one)
    for (int i = 0; i < n - 1; i++) {
        int mini = i; // Assume the smallest element is at the current position i


// Inner loop to find the smallest element in the unsorted part of the array
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[mini]) { // If a smaller element is found
                mini = j; // Update the position of the smallest element
            }
        }


 // Swap the smallest element found with the element at position i
        int temp = arr[mini];
        arr[mini] = arr[i];
        arr[i] = temp;
    }

 System.out.println("after selection sort ") ;
 for ( int i = 0 ; i < n ; i++) {
System.out.print(arr[i] + " ") ;
            
}
System.out.println() ;
}

//main function 
 public static void main(String[] args) {
         int arr[] = {13 , 46 , 24 , 52 , 20 , 9 };
         int n = arr.length ;
         System.out.println("before selection sort : ") ;
         for ( int i = 0 ; i < n ; i++){
             
             System.out.print(arr[i] + " ");
             
         }
         System.out.println();
         selection_sort(arr , n) ;
         
    }
}
```

## explanation 
#### What is Selection Sort?
Selection Sort is a simple sorting algorithm that works by repeatedly finding the minimum element from the unsorted part of the array and putting it at the beginning. The algorithm maintains two subarrays:

1) The subarray which is already sorted.
2) The remaining subarray which is unsorted.

   ![image](https://github.com/Mogana004/Leetcode_DSA/assets/92911280/3d9c4fad-4bf8-4f00-ab06-e1d4d7b7d6b1)


   ![image](https://github.com/Mogana004/Leetcode_DSA/assets/92911280/15f94cfc-9025-43a7-a6f6-fedf32fb4d50)

   ## GFG
   ![image](https://github.com/Mogana004/Leetcode_DSA/assets/92911280/191d2454-f7c1-4cf1-92f5-050bce5299a5)

