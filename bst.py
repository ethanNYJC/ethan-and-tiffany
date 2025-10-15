class Node:
    """
    creates a node object to be implemented in the BinarySearchTree class
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
  
class BinarySearchTree:
    """
    implements a binary search tree data structure
    """
    def __init__(self):
        self.root = None
  
    def is_empty(self):
        """
        checks if tree is empty
        """
        return self.root is None
    
    def insert(self, key):
        """
        creates a Node object and appropriately inserts it into the BST
        """
        new_node = Node(key)
        if self.is_empty():
            self.root = new_node
            return

        curr = self.root
        parent = None

        while curr:
            parent = curr
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                print("duplicate found. cannot insert")
                return

        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node            
    
    def search(self, key):
        """
        searches the BST for a key and returns True
        returns False if key cant be found
        """
        if self.is_empty():
            return False
        
        curr = self.root
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return True
        return False

    def delete(self, key):
        """
        kabooms the node
        """
        parent = None
        curr = self.root

        while curr and curr.key != key:
            parent = curr
            if key < curr.key:
                curr = curr.left
            else:
                curr = curr.right

        if curr is None:
            raise Exception("key cannot be found")

        if curr.left is None or curr.right is None:
            if curr.left:
                new_curr = curr.left
            else:
                new_curr = curr.right

        if parent is None:
            curr = new_curr
        elif parent.left.key == curr.key:
            parent.left = new_curr
        else:
            parent.right = new_curr

        successor_parent = curr
        successor = curr.right

        while successor.left:
            successor_parent = successor
            successor = successor.left

        curr.key = successor.key
        if successor_parent.left == successor:
            successor_parent.left = successor.right
        else:
            successor_parent.right = successor.right
