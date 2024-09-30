```java
import java.util.* ;
class HelloWorld {
    public static void main(String[] args) {
        int row = 2 ;
        int col = 2 ;
        Scanner sc = new Scanner(System.in) ;
        int[][] matrix1 = new int[row][col] ;
        int[][] matrix2 = new int[row][col] ;
        int[][] sum = new int[row][col] ;
        System.out.println("enter matrix 1:") ;
        for ( int i = 0 ; i< row ; i++){
            for ( int j = 0 ; j< col ; j++){
                matrix1[i][j] = sc.nextInt() ;
             }
            
        } 
       System.out.println(Arrays.deepToString(matrix1));
       
       
        System.out.println("enter matrix 2:");
        for ( int i = 0 ; i< row ; i++){
            for ( int j = 0 ; j< col ; j++){
                matrix2[i][j] = sc.nextInt() ;
                
                
            }
            
        }
        System.out.println(Arrays.deepToString(matrix2));
        
        System.out.println("addition of matrix1 and matrix2 is:") ;
        for ( int i = 0 ; i< row ; i++){
            for ( int j = 0 ; j< col ; j++){
                sum[i][j] = matrix1[i][j] + matrix2[i][j] ;
                System.out.print(sum[i][j] + " ");
                
             }
             System.out.println();
            
        }  
    }
}
```

![image](https://github.com/user-attachments/assets/57d64e28-78ce-4b05-a493-a70589338914)
