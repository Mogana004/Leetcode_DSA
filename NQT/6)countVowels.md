```java
class HelloWorld {
    public static void main(String[] args) {
      String str = "abc123!@#" ;
     strCounting(str) ;
      
    }
    public static void strCounting(String str){
        int vowels = 0 ;
        int consonents = 0 ;
        int digits = 0 ;
        int specialChars = 0 ;
        for ( int i = 0 ; i < str.length() ; i++){
            char ch = str.charAt(i); 
            
            if ( (ch >= 'a' && ch <= 'z') ||  
                (ch >= 'A' && ch <= 'Z') ) { 
                    ch = Character.toLowerCase(ch);
                   if ( ch  == 'a' || ch == 'e' || ch== 'i' || ch== 'o' || ch== 'u'){
                           vowels++ ;
                       
                   }
                else{
                   consonents++ ; 
                }
           } 
          else  if( ch >= '0' && ch <= '9' ){
               digits++ ;
           }
           else{
               specialChars++ ;
           }
    }
    System.out.println("digitcount:" + digits);
    System.out.println("vowelcount:" + vowels ) ;
    System.out.println("specialchars :" + specialChars ) ;
    System.out.println("consonentscount :" + consonents ) ;
            
        }
        
        
}
```
