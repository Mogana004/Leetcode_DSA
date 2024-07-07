```java
import java.util.* ;
class HelloWorld {
    public static void main(String[] args) {
        
        
        int[] arr = new int[]{ 1 , 2 , 3 , 3 , 4 , 1 } ;
        int[] visitedArr = new int[arr.length] ;
        int visited = -1 ;
        for ( int i = 0 ; i < arr.length ; i++){
            int count = 1 ;
            for ( int j =i+1 ; j <arr.length ; j++){
                if (arr[i] == arr[j]){
                    count++ ;
                    visitedArr[j] = visited ;
                }
            }
            if ( visitedArr[i] != visited){
                visitedArr[i] = count ;
            }
        }
        for (int i =0 ; i < visitedArr.length ; i++){
            if (visitedArr[i] != visited){
                System.out.println(arr[i]  + "="  + visitedArr[i]) ;
            }
        }
       
    }
   
}
```

### explanation
![image](https://github.com/Mogana004/Leetcode_DSA/assets/92911280/c1141c2c-8183-4ed7-8b9c-28c0d503e4eb)


