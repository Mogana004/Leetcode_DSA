```java
import java.util.* ;
class HelloWorld {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int arr[][] = new int[3][4] ; //2D array 
        for ( int i =0 ; i < 3 ; i++)  {
            for ( int j = 0 ; j < 4 ; j++)  {
                arr[i][j] =(int) (Math.random() * 100) ; //getting random input values for the array 
            }
            
        }
//printing the array 
        for ( int i =0 ; i < 3 ; i++)  {
            for ( int j = 0 ; j < 4 ; j++)  {
               System.out.print(arr[i][j] + " ") ;
               
            }
           System.out.println(); 
        }
        
    }
}
```
