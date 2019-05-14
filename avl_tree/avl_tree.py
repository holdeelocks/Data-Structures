import math
"""
Node class to keep track of
the data internal to individual nodes
"""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""


class AVLTree:
    def __init__(self, node=None):
        self.node = node
        # init height to -1 because of 0-indexing
        self.height = -1 if not node else 0
        self.balance = 0

    """
  Display the whole tree. Uses recursive def.
  """

    def display(self, level=0, pref=''):
        self.update_height()  # Update height before balancing
        self.update_balance()

        if self.node != None:
            print('-' * level * 2, pref, self.node.key, "[" + str(self.height) + ":" + str(
                self.balance) + "]", 'L' if self.is_leaf() else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.right != None:
                self.node.right.display(level + 1, '>')

    """
  Computes the maximum number of levels there are
  in the tree
  """

    def get_height(self):
        if self.node is None:
            return -1
        else:
            return self.height

    def update_height(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_height()
                if self.node.right != None:
                    self.node.right.update_height()

            self.height = max(-1 if not self.node.left else self.node.left.height,
                              -1 if not self.node.right else self.node.right.height) + 1
        else:
            self.height = -1

    """
  Updates the balance factor on the AVLTree class
  """

    def update_balance(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_balance()
                if self.node.right != None:
                    self.node.right.update_balance()

            self.balance = (self.node.left.height if self.node.left else -1) - \
                (self.node.right.height if self.node.right else -1)
        else:
            self.balance = 0

    """
  Perform a left rotation, making the right child of this
  node the parent and making the old parent the left child
  of the new parent.
  """

    def _left_rotate(self):
        A = self.node
        B = self.node.right.node
        T = B.left.node

        self.node = B
        B.left.node = A
        A.right.node = T

    """
  Perform a right rotation, making the left child of this
  node the parent and making the old parent the right child
  of the new parent.
  """

    def _right_rotate(self):
        A = self.node
        B = self.node.left.node
        T = B.right.node

        self.node = B
        B.right.node = A
        A.left.node = T

    """
  Sets in motion the rebalancing logic to ensure the
  tree is balanced such that the balance factor is
  1 or -1
  """

    def rebalance(self):
        self.update_height(False)
        self.update_balance(False)

        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left._left_rotate()
                    self.update_height()
                    self.update_balance()
                self._right_rotate()
                self.update_height()
                self.update_balance()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right._right_rotate()
                    self.update_height()
                    self.update_balance()
                self._left_rotate()
                self.update_height()
                self.update_balance()

    """
  Uses the same insertion logic as a binary search tree
  after the value is inserted, we need to check to see
  if we need to rebalance
  """

    def insert(self, key):
        newnode = Node(key)
        if not self.node:
            self.node = newnode
            self.node.left = AVLTree()
            self.node.right = AVLTree()
        elif key < self.node.key:
            self.node.left.insert(key)
        elif key > self.node.key:
            self.node.right.insert(key)

        self.rebalance()

    def is_leaf(self):
        return (self.height == 0)
