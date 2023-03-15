// HW Q10
/* The first method should return the height of this node. Remember that the
height of a leaf node is zero. The second method should print the data of every node in the subtree
rooted at this node using preorder traversal. */
public class TreeNode {
  private int data;
  private List<TreeNode> children;
  
  public int getHeight() {
    int height = 0;
    
    for(TreeNode child : children) {
      height = Math.max(height, child.getHeight() + 1);
    }
    return height;
  }
  
  public void traverse() {
    System.out.println(data);
    
    for(TreeNode child: children) {
      child.traverse();
    }
  }
  // Constructor and other methods not shown
}



// HW Q11
// Invert the subtree (reflect it over a vertical axis through this node).
public class BinaryTreeNode {
  private int value;
  private BinaryTreeNode leftChild;
  private BinaryTreeNode rightChild;
  
  public void invert() {
    BinaryTreeNode temp = leftChild;
    leftChild = rightChild;
    rightChild = temp;
    
    if(leftChild != null) {
      leftChild.invert();
    }
    if(rightChild != null) {
      rightChild.invert();
    }
  }
  // Constructor and methods not shown
}



// HW Q12
/* The first method removes the node with the largest value from the subtree rooted at this node
(assume this node is not largest). The second method returns the smallest value in the subtree
rooted at this node greater than or equal to n. If no such value exists, it returns null. */
public class BSTNode{
  private Integer value;
  private BSTNode left;
  private BSTNode right;
  
  public void deleteMax() {
    if(right.right != null) {
      right.deleteMax();
    }
    else {
      right = right.left;
    }
  }

  public Integer ceil(int n) {
    if(n > value) {
      if(right == null) {
        return null;
      }
      return right.ceil(n);
    }

    if(left == null) {
      return value;
    }

    Integer toReturn = left.ceil(n);
    if(toReturn != null) {
      return toReturn;
    }
    return value;
  }
  // Constructor and other methods not shown
}



// Feb 9th Lecture
public boolean insertBefore(E newValue, E value) {
  if(head.data.equals(value)) {
    head = new ListNode<E>(newValue, head);
    size++;
    return true;
  }
  
  ListNode<E> curr = head;
  while(curr.next != null) {
    if(curr.next.data.equals(value)) {
      curr.next = new ListNode(newValue, current);
      size++;
      return true;
    }
    curr = curr.next;
  }
  return false;
}


// Feb 14th Lecture
public class BinTreeNode<E> {
  private E data;
  private BinTreeNode<E> left;
  private BinTreeNode<E> right;
  
  // Constructors & simple methods not shown.
  
  public void preorder() {
    System.out.println(data);
    
    if(left != null)
      left.preorder();
    if(right != null)
      right.preorder();
  }
}

public void breadthFirst() {
  Queue<BinTreeNode<E>> q = new Queue<>();
  q.enqueue(this);
  
  while(!q.isEmpty()) {
    BinTreeNode<E> node = q.deque();
    System.out.println(node.data);
    
    if(node.left != null) {
      q.enqueue(node.left);
    }
    if(node.right != null) {
      q.enqueue(node.right);
    }
  }
}


// March 7th Lecture
public class Heap {
  private int[] arr = new int[10];
  private int size;
  
  public Heap() {} // Default constructor
  
  public Heap(int[] values) {
    size = values.length - 1;
    arr = values;
    for(int i = size/2; i >= 0; i--) {
      percolateDown(i);
    } 
  }
  
  public void insert(int num) {
    size++;
    if(size == arr.length) {
      // Double array size & copy elements
    }
    arr[size] = num;
    percolateUp(size);
  }
  
  public int removeMin() {
    int min = arr[i];
    arr[1] = arr[size];
    size--;
    percolateDown(1);
    return min;
  }
  
  public void decreaseKey(int index, int newValue) {
    arr[index] = newValue;
    percolateUp(index);
  }
  
  public void percolateUp(int index) {
    int num = arr[index];
    
    while(index > 1 && arr[index/2] > num) {
      arr[index] = arr[index/2];
      index /= 2;
    }
    arr[index] = num;
  }
  
  public void percolateDown(int index) {
    int num = arr[index];
    
    while(index*2 <= size) {
      if(num > arr[index*2] && (index*2 == size || arr[index*2] <= arr[index*2 + 1])) {
        arr[index] = arr[index*2];
        index *= 2;
      }
      else if(index*2 < size && (num > arr[index*2 + 1])) {
        arr[index] = arr[index*2 + 1];
        index = index*2 + 1;
      }
      else {
        break;
      }
    }
  }
}