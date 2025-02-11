```java
import java.util.*;
class Node{
    int data ;
    Node left ;
    Node right ;
    
    Node( int d){
        this.data = d ;
        this.left = null ;
        this.right = null ;
        
    }
}
class InOrderTraversal{
    public void inorder(Node root){
        if ( root == null) return ;
        inorder(root.left);
        
        System.out.print(root.data + " ");
        inorder(root.right);
        
    }
}

class BinaryTree{
  public static void main(String[] args) {
    Node  root = new Node(1);
    root.left = new Node(2);
    root.right = new Node(3);
    root.left.left = new Node(4);
    root.left.right = new Node(5);
    root.left.right.right = new Node(8);
     root.right.left = new Node(6);
    root.right.right = new Node(7);
   InOrderTraversal in = new InOrderTraversal();
    
    in.inorder(root);
    
  }
}
```
