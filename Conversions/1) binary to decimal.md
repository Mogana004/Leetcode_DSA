### 1) binary to decimal
```java
import java.util.* ;
class HelloWorld {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
          int s = sc.nextInt() ;
       System.out.println("the binary number is : " + s );
       int decimal = 0 ;
       int i = 0 ;
       while ( s != 0 ){
           int rem = s % 10 ;
           decimal = (int)(decimal + (rem * Math.pow(2 , i)));
           s = s/ 10 ;

          i++ ;
           
           
       }
       System.out.print(decimal );
 
       
    }
}
```
![binary2](https://github.com/user-attachments/assets/c0b03731-eba1-4ab4-96c9-efc60f74c639)
### output 
![image](https://github.com/user-attachments/assets/ca394d4e-68cb-4928-b866-76ae78e41732)
