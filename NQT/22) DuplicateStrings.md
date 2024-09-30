![image](https://github.com/user-attachments/assets/990d87a6-b21a-464e-a64a-1aab5a2cc39c)

```java
import java.util.* ;
class HelloWorld {
    public static void main(String[] args) {
        List<String> arraylist = new ArrayList<>() ;
       String[] array = { "apple" , "apple" , "orange" , "banana"  , "grapes" ,"orange" , "banana"} ;
       for ( int i = 0 ; i < array.length ; i++){
           for ( int j = i+1 ; j < array.length ; j++){
               if ( array[i].equals(array[j])){
                   arraylist.add(array[i]) ;
               }
               
           }
       }
    System.out.println( arraylist);
    }
}
```
## output 
[apple, orange, banana]
