class Node:
    #constructor
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val
    
    #pre order traversal 
    # root -> left -> right
    def preOrderTraversal(self):
        print(self.val,end=' ')
        if self.left:
            self.left.preOrderTraversal()
        if self.right:
            self.right.preOrderTraversal()

    #in order traversal
    # left -> root -> right
    def inOrderTraversal(self):
        if self.left:
            self.left.preOrderTraversal()
        print(self.val,end=' ')
        if self.right:
            self.right.preOrderTraversal()
    
    #post order traversal
    # left -> right -> root
    def inOrderTraversal(self):
        if self.left:
            self.left.preOrderTraversal()
        if self.right:
            self.right.preOrderTraversal()
        print(self.val,end=' ')

if __name__=="__main__":
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(5)
    root.left.right=Node(6)
    root.right.right=Node(4)
    root.inOrderTraversal()