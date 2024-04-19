![image](https://github.com/Mogana004/Leetcode_DSA/assets/92911280/df23c469-6a35-4d6b-8627-257e9c8def83)
## Explanation 
* We'll initialize two pointers: i and j. Pointer i will iterate through the array, and pointer j will keep track of the position to which the unique elements should be moved.
* We'll start iterating from the second element of the array since the first element is already considered unique.
* If the current element is equal to the previous element, we'll continue to the next element.
* If the current element is different from the previous element, we'll increment j and copy the current element to the position indicated by j.
* Finally, we'll return j + 1, which represents the length of the modified array.
