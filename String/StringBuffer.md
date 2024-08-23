```java
import java.util.* ;
class HelloWorld {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter a string :");
        
        String str = sc.nextLine() ;
        StringBuffer scb = new StringBuffer(str);  
        String rev = scb.reverse().toString() ;
        System.out.println(rev) ;
      
    }
    
}
```
### Explanation:
##### StringBuffer scb = new StringBuffer(original);

1) StringBuffer is a class in Java used to create mutable strings. 
2) Unlike String, which is immutable (cannot be changed once created), StringBuffer allows modifications such as appending, deleting, and reversing characters.
3) new StringBuffer(original) creates a new StringBuffer object initialized with the content of the string original. This means scb now holds a mutable version of the original string.
4) scb is the variable name that refers to this StringBuffer object.

 ##### String rev = scb.reverse().toString();

1) scb.reverse() is a method call that reverses the sequence of characters in the StringBuffer object scb. After this method is called, the characters in scb are reversed, but scb itself remains a StringBuffer object.
2) toString() is a method that converts the StringBuffer object back into a String. After reversing, you want the result as a String, not as a StringBuffer.
3) String rev is a variable that holds the reversed string result after the conversion
