class RBNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.colour = "R"

    def get_uncle(self):
        return

    def is_leaf(self):
        return self.left == None and self.right == None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()

    def is_red(self):
        return self.colour == "R"

    def is_black(self):
        return not self.is_red()

    def make_black(self):
        self.colour = "B"

    def make_red(self):
        self.colour = "R"

    def get_brother(self):
        if self.parent.right == self:
            return self.parent.left
        return self.parent.right

    def get_uncle(self):
        return self.parent.get_brother()

    def uncle_is_black(self):
        if self.get_uncle() == None:
            return True
        return self.get_uncle().is_black()

    def __str__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def __repr__(self):
         return "(" + str(self.value) + "," + self.colour + ")"

    def rotate_right(self):
        new_root = self.left
        self.left = new_root.right

        if new_root.right != None:
            new_root.right.parent = self

        new_root.parent = self.parent

        if self.parent == None:
            self.root = new_root
        elif self.is_left_child():
            self.parent.left = new_root
        else:
            self.parent.right = new_root
        new_root.right = self
        self.parent = new_root


    def rotate_left(self):
        # save the right child of the current node as the new root
        new_root = self.right
        # assign the left subtree of the new root to be the right subtree of the old root
        self.right = new_root.left

        # update the parent pointer of the left subtree of the new root
        if new_root.left != None:
            new_root.left.parent = self

        # update the parent pointer of the new root
        new_root.parent = self.parent

        # update the parent pointer of the old root's parent to point to the new root
        if self.parent == None:
            self.root = new_root
        elif self.is_left_child():
            self.parent.left = new_root
        else:
            self.parent.right = new_root
        new_root.left = self
        # update the parent pointer of the old root to point to the new
        self.parent = new_root


class RBTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def insert(self, value):
        if self.is_empty():
            self.root = RBNode(value)
            self.root.make_black()
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = RBNode(value)
                node.left.parent = node
                self.fix(node.left)
            else:
                self.__insert(node.left, value)
        else:
            if node.right == None:
                node.right = RBNode(value)
                node.right.parent = node
                self.fix(node.right)
            else:
                self.__insert(node.right, value)

def fix(self, node):
    # If node's parent is None, it means the node is the root and must be black.
    if node.parent == None:
        node.make_black()
    
    # Loop until node is not None, node's parent is not None, and node's parent is black.
    while node != None and node.parent != None and node.parent.is_red():
        
        # If node's parent is a left child of its grandparent.
        if node.parent.is_left_child():
            
            # Get node's uncle (right child of grandparent).
            uncle = node.get_uncle()
            
            # If node's uncle is red, then recolor parent, uncle, and grandparent.
            if uncle != None and uncle.is_red():
                node.parent.make_black()
                uncle.make_black()
                node.parent.parent.make_red()
                node = node.parent.parent
            else:
                # If node is a right child, then rotate left around parent to make it a left child.
                if node.is_right_child():
                    node = node.parent
                    node.rotate_left()
                
                # Recolor parent and grandparent, and rotate right around grandparent.
                node.parent.make_black()
                node.parent.parent.make_red()
                node.parent.parent.rotate_right()
                
        # If node's parent is a right child of its grandparent.
        else:
            
            # Get node's uncle (left child of grandparent).
            uncle = node.get_uncle()
            
            # If node's uncle is red, then recolor parent, uncle, and grandparent.
            if uncle != None and uncle.is_red():
                node.parent.make_black()
                uncle.make_black()
                node.parent.parent.make_red()
                node = node.parent.parent
            else:
                # If node is a left child, then rotate right around parent to make it a right child.
                if node.is_left_child():
                    node = node.parent
                    node.rotate_right()
                
                # Recolor parent and grandparent, and rotate left around grandparent.
                node.parent.make_black()
                node.parent.parent.make_red()
                node.parent.parent.rotate_left()
    
    # Finally, make sure the root is black.
    self.root.make_black()


    def __str__(self):
        if self.is_empty():
            return "[]"
        return "[" + self.__str_helper(self.root) + "]"

    def __str_helper(self, node):
        if node.is_leaf():
            return "[" + str(node) + "]"
        if node.left == None:
            return "[" + str(node) + " -> " + self.__str_helper(node.right) + "]"
        if node.right == None:
            return "[" +  self.__str_helper(node.left) + " <- " + str(node) + "]"
        return "[" + self.__str_helper(node.left) + " <- " + str(node) + " -> " + self.__str_helper(node.right) + "]"
