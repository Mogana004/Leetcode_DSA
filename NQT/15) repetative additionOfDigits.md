![image](https://github.com/user-attachments/assets/7473ef58-fba5-4e7a-8ace-5d7be275f757)

```java
class Solution{
    static int singleDigit(long N){
        if ( N <= 9 ){
            return (int) N ;
        }
       while ( N > 9 ){
           int sum = 0 ;
           
           while ( N > 0 ){
               int digit =(int) (N % 10) ;
               sum = sum + digit ;
               N = N / 10 ;
               
           }
         N = sum ;
           
       }
     return (int)N;
       
    }
}
```
