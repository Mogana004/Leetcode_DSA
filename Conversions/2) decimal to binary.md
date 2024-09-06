## 2) Decimal to binary.
```java
import java.util.* ;
class HelloWorld {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
          int s = sc.nextInt() ;
          StringBuilder sb = new StringBuilder() ;
          while( s != 0 ){
              int rem = s % 2 ;
              sb.append(rem) ;
              
              s = s/ 2 ;
          }
          String b = sb.reverse().toString() ;
          System.out.print(b);
          
    }
}
```
![image](https://github.com/user-attachments/assets/c020fc4e-467b-4eb6-b436-50e5f74cf7d4) 
## output 
![image](https://github.com/user-attachments/assets/c20a2c86-1b2f-46c8-94c5-f7eeba4fa259)

