
```java

public class Stack {
    int stack[] = new int[5]; // Stack with a fixed size
    int top = 0; // Pointer to the top of the stack

    // Push method
    public void push(int data) {
        if (top < stack.length) { // Check if there is space in the stack
            stack[top] = data;
            top++;
            System.out.println(data + " pushed to the stack.");
        } else {
            System.out.println("Stack overflow! Cannot push " + data);
        }
    }

    // Pop method (optional)
    public int pop() {
        if (top > 0) {
            top--;
            return stack[top];
        } else {
            System.out.println("Stack underflow! No elements to pop.");
            return -1; // Return an invalid value when the stack is empty
        }
    }
}

class HelloWorld {
    public static void main(String[] args) {
        Stack nums = new Stack(); // Create a Stack object
        nums.push(15); // Push values to the stack
        nums.push(6);
        nums.push(10);
        nums.push(20);
        nums.push(25); // This will be the last element to fit in the stack
        nums.push(30); // This will trigger a stack overflow message
    }
}
```
