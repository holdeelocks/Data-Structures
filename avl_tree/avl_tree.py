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

    def update_height(self):
        # if not self.node.left and not self.node.right:
        #     self.height += 1
        # else:
        #     self.height = max(self.node.left.get_height() if self.node.left else 0,
        #                       self.node.right.get_height() if self.node.right else 0) + 1
        if self.node.left and self.node.right:
            self.height = max(self.node.left.get_height(),
                              self.node.right.get_height()) + 1
        elif self.node.left:
            self.height = self.node.left.get_height() + 1
        elif self.node.right:
            self.height = self.node.right.get_height() + 1
        elif self.node:
            self.height = 0

    """
  Updates the balance factor on the AVLTree class
  """

    def update_balance(self):
        if not self.node or (not self.node.left and not self.node.right):
            self.balance = 0
        elif self.node.left and self.node.right:
            self.balance = self.node.left.height - self.node.right.height
        else:
            if self.node.left:
                self.balance = self.node.left.height
            if self.node.right:
                self.balance = 0 - self.node.right.height

    """
  Perform a left rotation, making the right child of this
  node the parent and making the old parent the left child
  of the new parent.
  """

    def _left_rotate(self):
        new_root = self.node.right.node
        self.node.right.node = new_root.left.node
        if new_root.left.node != None:
            self.node.right.node = new_root.left.node
        new_root.left.node = self.node
        self.node = new_root

        # self.balance = self.balance + 1 + max(self.balance, 0)
        # self.node.left.balance = self.node.left.balance + \
        #     1 - min(self.node.left.balance, 0)

        # self.update_height()
        # self.node.left.update_height()

    """
  Perform a right rotation, making the left child of this
  node the parent and making the old parent the right child
  of the new parent.
  """

    def _right_rotate(self):
        new_root = self.node.left.node
        self.node.left.node = new_root.right.node
        if new_root.right.node != None:
            self.node.left.node = new_root.right.node
        new_root.right.node = self.node
        self.node = new_root

        # self.balance = self.balance + max(self.balance, 0)
        # self.node.right.balance = self.node.right.balance - \
        #     min(self.node.right.balance, 0)

        # self.update_height()
        # self.node.right.update_height()

    """
  Sets in motion the rebalancing logic to ensure the
  tree is balanced such that the balance factor is
  1 or -1
  """

    def rebalance(self):
        self.update_height()
        if self.balance < 0:
            if self.node.right.balance > 0:
                self.node.right._right_rotate()
                self.node._left_rotate()
            else:
                self.node._left_rotate()
        elif self.balance > 0:
            if self.node.left.balance < 0:
                self.node.left._left_rotate()
                self.node._right_rotate()
            else:
                self.node._right_rotate()
    """
  Uses the same insertion logic as a binary search tree
  after the value is inserted, we need to check to see
  if we need to rebalance
  """

    def insert(self, key):
        if not self.node:
            self.node = Node(key)
        elif key < self.node.key:
            if self.node.left:
                self.node.left.insert(key)
                # self.update_height()
            else:
                self.node.left = AVLTree(Node(key))
                # self.node.left.rebalance()
        else:
            if self.node.right:
                self.node.right.insert(key)
                # self.node.right.update_height()
            else:
                self.node.right = AVLTree(Node(key))
                # self.node.right.rebalance()

        # self.update_height()
        self.update_balance()
        if self.balance > 1 or self.balance < -1:
            self.rebalance()

    def is_leaf(self):
        return not self.node.left and not self.node.right
