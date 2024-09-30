![image](https://github.com/user-attachments/assets/2cdb611d-dd07-424e-8d48-1ff85f30c9fa)
```java
import java.util.Scanner ;
class HelloWorld {
    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in) ;
       int weight = sc.nextInt() ;
       int distance = sc.nextInt() ;
       float a=  callfunction(weight , distance ) ;
       System.out.printf( "%.2f",a) ;
    }
    public static float callfunction(int weight , int distance ){
       double formula = 5   + ( weight * 2  ) + ( (distance / 10) * 0.5);
        return (float) formula ;
        
    }
}
```
### note :
To get with two decimal points .. 
1) format the output - using printf ( "%.2f",a) 
