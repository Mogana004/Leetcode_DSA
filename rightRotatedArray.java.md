## code 
```java
import java.util.Scanner;
class Main {
    public static void main(String[] args) { 
        Scanner sc= new Scanner(System.in);
        
        //Read N
        int N= sc.nextInt();
        
        //read the Array
        int[] array = new int[N];
        for (int i= 0 ; i < N ; i++){
            array[i] = sc.nextInt();
        }
       
       //read k
       int k = sc.nextInt();
       
       // right rotate the array by k positions 
       int[] rotatedArray = new int[N];
       for (int i=0 ; i <N ; i++){
           rotatedArray[(i+k) % N] = array[i];
        }
       
       //print the rotated array 
       for (int i = 0 ; i <N ; i++){
           System.out.print(rotatedArray[i]);
           if (i <N-1 ){
               System.out.print(" ");
              }
       }
       System.out.println();
    }
}
```

## input and output 
5
1 2 3 4 5
3


output: 3 4 5 1 2

