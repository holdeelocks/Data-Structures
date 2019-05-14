class Heap:
    def __init__(self, comparator=None):
        self.storage = []
        self.comparator = (
            lambda x, y: x > y) if comparator == None else comparator

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(self.get_size() - 1)

    def delete(self):
        if self.get_size() == 1:
            return self.storage.pop()
        max_item = self.storage[0]
        self.storage[0] = self.storage.pop()
        self._sift_down(0)

        return max_item

    def get_priority(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        curr_val = self.storage[index]
        parent_idx, parent_val = self._get_parent(index)
        if index > 0 and self.comparator(curr_val, parent_val):
            self.storage[parent_idx], self.storage[index] = curr_val, parent_val
            self._bubble_up(parent_idx)
        return

    def _get_parent(self, index):
        if index == 0:
            return None, None
        parent_idx = (index - 1) // 2
        return parent_idx, self.storage[parent_idx]

    def _sift_down(self, index):
        curr_val = self.storage[index]
        left_child_idx, right_child_idx = 2 * index + 1, 2 * index + 2

        if left_child_idx > self.get_size() - 1:
            left_child_idx, left_child_val = None, None
        else:
            left_child_val = self.storage[left_child_idx]

        if right_child_idx > self.get_size() - 1:
            right_child_idx, right_child_val = None, None
        else:
            right_child_val = self.storage[right_child_idx]

        best_child_idx, best_child_val = left_child_idx, left_child_val

        if right_child_idx is not None and self.comparator(right_child_val, left_child_val):
            best_child_idx, best_child_val = right_child_idx, right_child_val

        if best_child_idx is not None and self.comparator(best_child_val, curr_val):
            self.storage[index], self.storage[best_child_idx] = best_child_val, curr_val
            self._sift_down(best_child_idx)

        return
