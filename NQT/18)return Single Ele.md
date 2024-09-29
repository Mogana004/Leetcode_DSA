 # Return Single Element in an array 
```java
class HelloWorld {
    public static void main(String[] args) {
        int nums[] = { 1 ,2  ,1 ,4 , 4 , 3 ,2 } ;
        System.out.println(singleElement(nums)) ;
        
    }
    public static int singleElement(int nums[] ){
        int length = nums.length ;
        for ( int i = 0 ; i < length ; i++){
            int num = nums[i] ;
            int count = 0 ;
            for ( int j= 0 ; j < length ;j++){
                if ( num == nums[j]){
                    count++ ;
                }
               
            }
             if ( count != 2 ){
                    return num ;
                }
        }
        return -1 ;
    }
}
```
## optimal approach 

```java
class HelloWorld {
    public static void main(String[] args) {
        int nums[] = { 1 ,2  ,1 ,4 , 4 , 3 ,2 } ;
        System.out.println(singleElement(nums)) ;
        
    }
    public static int singleElement(int nums[] ){
       int xor = 0 ;
       for ( int i = 0 ; i < nums.length ;i++){
           xor = xor ^ nums[i] ;
           
       }
       return xor ;
    }
}
```
