![image](https://github.com/Mogana004/Leetcode_DSA/assets/92911280/ad2b8dd2-c08b-4956-a3f8-bb05d67ee52e)


## program 
```java
import java.util.Scanner;
class Main {
    public static void main(String[] args) { 
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        int[] A = new int[N];
        for (int i= 0 ; i< N ; i++){
            A[i] = sc.nextInt();
        }
        int  pointer1 = 0;
        int pointer2 = A.length - 1 ;
        boolean pairFound = false;
        while (pointer1 < pointer2){
            int sum = A[pointer1] + A[pointer2] ;
            if ( sum== K){
                System.out.println((pointer1 ) + " " +(pointer2 ));
                pointer1++;
                pointer2--;
               pairFound = true;
            }
            else if (sum < K ){
                pointer1++;
            }
            else {
                pointer2--;
            }
        }
        if( !pairFound){
            System.out.println("-1");
        }
    
    }
}
```
