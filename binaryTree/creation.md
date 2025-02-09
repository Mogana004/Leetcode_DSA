```java
class Node {
    int data;
    Node left, right;

    // Constructor to create a new node
    Node(int data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

class BinaryTree {
    public static void main(String[] args) {
        // Manually creating the binary tree
        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.left.left = new Node(4);
        root.left.right = new Node(5);
        root.right.left = new Node(6);
        root.right.right = new Node(7);

        // Printing the root node
        System.out.println("Root.left Node: " + root.right.data);
    }
}
```
