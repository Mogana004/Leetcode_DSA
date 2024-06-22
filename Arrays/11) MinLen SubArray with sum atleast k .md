
```java
import java.util.Scanner;
class Main {
    public static void main(String[] args) { 
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        
        int[] array = new int[N];
        for (int i= 0 ; i < N ;i++){
            array[i] = sc.nextInt();
            
        }
        int minLength = Integer.MAX_VALUE ;
        int currentSum = 0 ;
        int left = 0 ;
        
        for (int right = 0 ; right <N ; right++){
           currentSum += array[right];
           
           while (currentSum >= K){
               minLength = Math.min(minLength , right- left +1);
               currentSum -= array[left];
               left++;
               
           }
        }
        if (minLength == Integer.MAX_VALUE){
            System.out.println(0);
        }
        else{
          System.out.println(minLength);   
        }
       
    }
}

```
