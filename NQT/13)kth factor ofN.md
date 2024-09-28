###  kth factor of n 
![image](https://github.com/user-attachments/assets/5dffe475-22b4-4d09-8a17-b40944a6fe9e)

```java

import java.util.* ;
class HelloWorld {
    public static void main(String[] args) {
        int n = 24 ;
        int k = 2 ;
        List<Integer> arr = new ArrayList<>() ;
        
        for ( int i = 1 ; i < n ; i++){
            if ( n % i == 0){
                arr.add(i) ;
                
            }
        }
        Collections.sort(arr , Collections.reverseOrder()) ;
       // Check if k exceeds the number of factors
        if (k > arr.size()) {
           System.out.println("1") ;  
        } else {
           System.out.println(arr.get(k - 1));  
        }
    }
}
```
