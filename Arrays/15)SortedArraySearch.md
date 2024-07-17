## question - Sorted array Search 
#### Given an array arr[] sorted in ascending order of size N and an integer K. Check if K is present in the array or not.
```java
class Solution{
    static int searchInSorted(int arr[], int N, int K)
    {
        
        
     for ( int i = 0 ; i < N ; i++){
         if ( arr[i] == K ){
             return 1 ;
         }
     }
     return -1 ;
    }
}```
![image](https://github.com/user-attachments/assets/c11082a2-b11b-4f8d-b322-3f6dc4b122ab)
https://www.geeksforgeeks.org/problems/who-will-win-1587115621/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=who-will-win
