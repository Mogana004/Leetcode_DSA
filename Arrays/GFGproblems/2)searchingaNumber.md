## [searchingaNumber](https://www.geeksforgeeks.org/problems/searching-a-number0324/1?page=2&category=Arrays&sortBy=difficulty)
Given an integer k and array arr. Your task is to return the position of the first occurrence of k in the given array and if element k is not present in the array then return -1.

Note: 1-based indexing is followed here.
```java
class Solution {
    public int search(int k, ArrayList<Integer> arr) {
        int length = arr.size();
        for (int i = 0; i < length; i++) {
            if (arr.get(i) == k) {
                return i + 1;  // Return one-based index
            }
        }
        return -1;  // Return -1 if element is not found after the loop
    }
}
```
