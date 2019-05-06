class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        new_node = BinarySearchTree(value)

        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = new_node
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = new_node
                else:
                    self.right.insert(value)
        else:
            self.value = value

    def contains(self, target):
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        elif target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        else:
            return True

    def get_max(self):
        curr = self
        while curr.right:
            curr = curr.right

        return curr.value

    def for_each(self, cb):
        curr = self
        cb(self.value)

        if curr.left:
            curr.left.for_each(cb)
        if curr.right:
            curr.right.for_each(cb)
