## Left rotate the array by 1 place 
#### optimal approach 

class HelloWorld {
    public static void main(String[] args) {
        int[] array = { 1 , 2 ,3 , 4 , 5 };
        int n = array.length ;
        int temp = array[0] ;
        for ( int i = 1 ; i < n ; i++){
            array[i-1] = array[i] ;
            
        }
        array[n-1] = temp ;
        for ( int i = 0 ; i < n ; i++){
            System.out.print(array[i] +  " ") ;
        }
    }
}![image](https://github.com/user-attachments/assets/fdecc503-e59e-4c47-9e9f-d29c5b0271b5)
![image](https://github.com/user-attachments/assets/b044b1f0-4981-421a-9d6a-c2a78f361b9f) 

