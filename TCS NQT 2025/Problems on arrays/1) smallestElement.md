## 1) smallestElement 
  ```java
import java.util.Scanner ;
class HelloWorld {
    public static void main(String[] args) {
        Scanner sc =  new Scanner(System.in) ;
        int length = 6 ;
        int arr[] = new int[length ];
        System.out.println("enter the array elements :");
        for ( int i = 0 ; i < length ; i++){
            arr[i] = sc.nextInt() ;
            
        }
        int small = arr[0] ;
        for ( int i = 0 ; i < length ; i++){
            if ( arr[i] < small){
                small = arr[i] ;
                
            }
           
        }
         System.out.println("the smallest element in the array is : " + small);
        
    }
}
```
