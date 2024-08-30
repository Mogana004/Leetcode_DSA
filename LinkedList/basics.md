## Basics 
```java
class Node {
    int data;
    Node next;

    // Constructor with data and next node
    Node(int data1, Node next1) {
        this.data = data1; // Assign data1 to the instance variable 'data'
        this.next = next1; // Assign next1 to the instance variable 'next'
    }

    // Constructor with only data (next is null)
    Node(int data1) {
        this.data = data1; // Assign data1 to the instance variable 'data'
        this.next = null;  // Set next to null
    }
}

class LinkedList {
    public static void main(String[] args) {
        int[] arr = {2, 5, 6, 7, 8, 9}; // Array of integers

        // Create a Node using the value at index 3 in the array (which is 7)
        Node y = new Node(arr[3]);

        // Print the data stored in the node
        System.out.println(y.data);
    }
}
```

#### output

- C:\Users\ACER\Documents>javac LinkedList.java

- C:\Users\ACER\Documents>java LinkedList

 7
