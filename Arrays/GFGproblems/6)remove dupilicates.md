```java
class Solution {
    // Function to remove duplicates from the given array
    public int remove_duplicate(List<Integer> arr) {
        
        int n = arr.size();
        if (n == 0) return 0; // Handle empty list

        int i = 0;
        for (int j = 1; j < n; j++) {
            if (!arr.get(i).equals(arr.get(j))) {
                i++;
                arr.set(i, arr.get(j));
            }
        }
        
        // Resize the list to contain only the unique elements
        for (int k = n - 1; k > i; k--) {
            arr.remove(k);
        }

        return i + 1; // New length after removing duplicates
    }
}

    
```
