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