![image](https://github.com/Mogana004/Leetcode_DSA/assets/92911280/196fb855-4a02-4dc7-ba97-dd604fbfddd8)
![image](https://github.com/Mogana004/Leetcode_DSA/assets/92911280/e4a9a17a-d345-48c6-90c4-f23a64e903a8)

## code 

```java
import java.util.Scanner;
class Main {
    public static void main(String[] args) { 
        int count = 0 ;
        int maxcount = 0;
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] A = new int[N] ;
        for (int i=0 ; i<N ; i++ ){
            A[i] = sc.nextInt();
       }
        for (int eachnum :A){
            if (eachnum == 1){
               count++ ;
               maxcount = Math.max(maxcount , count );
            }
            else{
                count = 0 ;
            }
        }    
        System.out.print(maxcount);
    
    }
}
```
