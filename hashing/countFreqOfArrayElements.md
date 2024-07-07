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

If Array = {1 , 2, 1 , 3, 2 ,4 }  , 
the frequency of each elements will be 
```
1 2
2 2
3 1
4 1 
```
