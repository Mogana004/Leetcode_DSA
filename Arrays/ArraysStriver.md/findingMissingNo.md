## approach 1) better 
```java
class HelloWorld {
    public static void main(String[] args) {
        // expected sum 
        int n = 5 ;
        int expectedsum = n * (n+1) / 2 ; 
        int actualsum = 0 ;
        int[] arr = {1 , 2, 3 ,5} ;
        for ( int i = 0 ; i < n-1 ; i++){
            actualsum += arr[i] ;
            
        }
     System.out.print(expectedsum - actualsum) ;
        
        
    }
}
```

### explanation 


####  Steps:
##### Calculate the expected sum of the first N natural numbers.
##### Calculate the actual sum of the elements in the array.
##### The difference between the expected sum and the actual sum is the missing number.
![image](https://github.com/user-attachments/assets/1c1999b0-66c0-4ee2-affa-15143046a5d1)
