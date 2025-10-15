from bst import BinarySearchTree

if __name__ == "__main__":
    # Test your code with the following data
    bst = BinarySearchTree()
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(5)
    print(bst.search(4)) # returns False
    print(bst.search(7))  # returns True
    