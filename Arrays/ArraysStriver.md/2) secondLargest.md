# brute force approach :
steps :
1) sort the array
2) print  array[1] for second smallest element
3) and print array[ n- 2] index for the second largest element

   ![image](https://github.com/Mogana004/Leetcode_DSA/assets/92911280/3726fdb8-5040-4d49-815c-a560bdd2838e)

# better approach 

```java
class HelloWorld {
    public static void main(String[] args) {
        int arr[] = {1 , 2 , 3, 5 ,9 , 7} ;
        int N = arr.length ;
        int max = Integer.MIN_VALUE ;
       int second_max =  Integer.MIN_VALUE ;
      
        for ( int i = 0 ; i < N ; i++){
            
            if ( arr[i] > max ){
                max = arr[i] ;
               
            }
            
            
        }
        for ( int i = 0 ; i < N ; i++){
           if (arr[i] > second_max  && arr[i] != max){
               second_max = arr[i];
           }
        }
        
        System.out.println(max) ;
        System.out.println(second_max);
        
    }
}
```
# optimal approach 
steps :
1)  need to do two traversals
2)  one traversal is to find the largest of the array
3)  and the other is to find the second large which initializes a variable with min value and also checks whether the second largest value is not equal to the largest .


![image](https://github.com/Mogana004/Leetcode_DSA/assets/92911280/ddddd5bd-0f69-49b8-aa93-4b9cfb8064ce)
