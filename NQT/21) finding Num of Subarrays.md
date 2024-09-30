```java

class HelloWorld {
    public static void main(String[] args) {
       int array[] = { 1 ,2 ,4 , 6 , 1 ,2 , 3 } ;
       int k = 6 ;
       System.out.println(subarray( array , k ));
    }
    public static int subarray(int array[] , int k){
        int count = 0 ; 
        for ( int i = 0 ; i < array.length ; i++){
            int sum = 0 ;
            for ( int j = i ; j < array.length ; j++){
                sum = sum + array[j] ;
                if ( sum == k ){
                    count= count + 1 ;
                }
            }
        }
        return count ; 
    }
}
```
