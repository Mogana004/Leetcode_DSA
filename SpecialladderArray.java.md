```java
import java.util.Scanner;
class Main {
 public static void main(String[] args) { 
  Scanner sc = new Scanner(System.in);
  int n = sc.nextInt();
  
  int[] array = new int[n];
  for (int i= 0 ; i <n;i++){
      array[i] = sc.nextInt();
      
  }
  int special = array[n-1];
  int count = 1 ;
  
  for (int i = n-2 ; i >=0 ; i--){
      if (array[i] > special) {
          count++ ;
          special = array[i];
      }
  }
  System.out.println(count);
  
  }
}

```

## Question
To complete the code for the special ladder question, 
we need to calculate the count of numbers that are always greater than the 
digits to their right and then print that count along with the 
last element as the special element. Here's the completed code:
