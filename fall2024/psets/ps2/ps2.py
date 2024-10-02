class BinarySearchTree:
    # left: BinarySearchTree
    # right: BinarySearchTree
    # key: int
    # item: int
    # size: int
    def __init__(self, debugger=None):
        self.left = None
        self.right = None
        self.key = None
        self.item = None
        self._size = 1
        self.debugger = debugger

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, a):
        debugger = self.debugger
        if debugger:
            debugger.inc_size_counter()
        self._size = a

    ####### Part a #######
    """
    Calculates the size of the tree
    returns the size at a given node
    """

    def calculate_sizes(self, debugger=None):
        # Debugging code
        # No need to modify
        # Provides counts
        if debugger is None:
            debugger = self.debugger
        if debugger:
            debugger.inc()

        # Implementation
        self.size = 1
        if self.right is not None:
            self.size += self.right.calculate_sizes(debugger)
        if self.left is not None:
            self.size += self.left.calculate_sizes(debugger)
        return self.size

    """
    Select the ind-th key in the tree
    
    ind: a number between 0 and n-1 (the number of nodes/objects)
    returns BinarySearchTree/Node or None
    """

    def select(self, ind):
        left_size = 0
        if self.left is not None:
            left_size = self.left.size
        if ind == left_size:
            return self
        if left_size > ind and self.left is not None:
            return self.left.select(ind)
        if left_size < ind and self.right is not None:
            # We need to adjust for the left subtree's nodes that we're no longer counting
            return self.right.select(ind - left_size - 1)
        return None

    """
    Searches for a given key
    returns a pointer to the object with target key or None (Roughgarden)
    """

    def search(self, key):
        # This is correct
        if self is None:
            return None
        elif self.key == key:
            return self
        elif key > self.key and self.right is not None:
            return self.right.search(key)
        elif key < self.key and self.left is not None:
            return self.left.search(key)
        return None

    """
    Inserts a key into the tree
    key: the key for the new node; 
        ... this is NOT a BinarySearchTree/Node, the function creates one
    
    returns the original (top level) tree - allows for easy chaining in tests
    """

    def insert(self, key):
        if self.key is None:
            self.key = key
        elif self.key > key:
            if self.left is None:
                self.left = BinarySearchTree(self.debugger)
            self.left.insert(key)
            self.size += 1
        elif self.key < key:
            if self.right is None:
                self.right = BinarySearchTree(self.debugger)
            self.right.insert(key)
            self.size += 1
        return self

    ####### Part b #######

    """
    Performs a `direction`-rotate the `side`-child of (the root of) T (self)
    direction: "L" or "R" to indicate the rotation direction
    child_side: "L" or "R" which child of T to perform the rotate on
    Returns: the root of the tree/subtree
    Example:
    Original Graph
      10
       \
        11
          \
           12
    
    Execute: NodeFor10.rotate("L", "R") -> Outputs: NodeFor10
    Output Graph
      10
        \
        12
        /
       11 
    """

    def rotate(self, direction, child_side):
        # Algorithm
        # Root is self

        # Node we are choosing to rotate
        # 'B'
        rotation_node = self.right if child_side == "R" else self.left

        # Prep for rotation
        # y = 'D'
        y = rotation_node.left if direction == "R" else rotation_node.right
        if child_side == "R":
            self.right = y
        else:
            self.left = y
            # A.left = 'D'

        # a, b, c are pointers that will be reassigned
        if direction == "R":
            a = rotation_node.right  # 'E'
            b = y.right  # None
            c = y.left  # None
        else:
            a = rotation_node.left
            b = y.left
            c = y.right

        if direction == "R":
            rotation_node.left = b  # 'B'.left = None
            y.right = rotation_node  # 'D'.right = 'B'
        else:
            rotation_node.right = b
            y.left = rotation_node

        # sizes
        if a:
            y.size += 1 + a.size
        else:
            y.size += 1
        if c:
            rotation_node.size -= 1 + c.size
        else:
            rotation_node.size -= 1

        return self

    def print_bst(self):
        if self.left is not None:
            self.left.print_bst()
        print(self.key),
        if self.right is not None:
            self.right.print_bst()
        return self
