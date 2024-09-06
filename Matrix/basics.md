## Method 1 - getting the array input and  printing the array using nestedloop . 
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
 
        for ( int i =0 ; i < 3 ; i++)  {
            for ( int j = 0 ; j < 4 ; j++)  {
               System.out.print(arr[i][j] + " ") ;
               
            }
           System.out.println(); 
        }
        
    }
}
```

## method2 -  printing the array using for each loop 
```java
import java.util.* ;
class HelloWorld {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int arr[][] = new int[3][4] ; //2D array 
        for ( int i =0 ; i < 3 ; i++)  {
            for ( int j = 0 ; j < 4 ; j++)  {
                arr[i][j] =(int) (Math.random() * 100) ;
            }
            
        }
// for each loop 
       for ( int eacharray[] : arr){ 
           for ( int num : eacharray){
               System.out.print(num + " ");
               
           }
           System.out.println();
           
       }
        
    }
}
```
### output :
 75 97 47 69 
 33 97 78 54 
 85 2 68 31 

