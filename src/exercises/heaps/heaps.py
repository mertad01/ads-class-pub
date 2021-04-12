#!/usr/bin/env python3
"""
`heaps` implementation

@author: Adam Mertzenich
"""

# Question #1:
# [42, 35, 71, 34, 76, 39, 77, 47, 6, 20]
# [42, 35, 71, 34, 20, 39, 77, 47, 6, 76]
# [42, 35, 71, 6, 20, 39, 77, 47, 34, 76]
# [42, 35, 39, 6, 20, 71, 77, 47, 34, 76]
# [42, 6, 39, 34, 20, 71, 77, 47, 35, 76]
# [6, 20, 39, 34, 42, 71, 77, 47, 35, 76]



from typing import Any, List


class BinaryHeapMin:
    """Min Heap class implementation"""
    def __init__(self):
        """Initializer"""
        self._heap: List[Any] = []
        self._size = 0

    def perc_up(self, cur_idx: int):
        """Move a node up"""
        while (cur_idx - 1) // 2 >= 0:
            parent_idx = (cur_idx - 1) // 2
            if self._heap[cur_idx] < self._heap[parent_idx]:
                self._heap[cur_idx], self._heap[parent_idx] = (
                    self._heap[parent_idx],
                    self._heap[cur_idx],
                )
            cur_idx = parent_idx

    def perc_down(self, cur_idx: int):
        """Move a node down"""
        while 2 * cur_idx + 1 < len(self._heap):
            min_child_idx = self._get_min_child(cur_idx)
            if self._heap[cur_idx] > self._heap[min_child_idx]:
                self._heap[cur_idx], self._heap[min_child_idx] = (
                    self._heap[min_child_idx],
                    self._heap[cur_idx],
                )
            else:
                return
            cur_idx = min_child_idx

    def _get_min_child(self, parent_idx):
        if 2 * parent_idx + 2 > len(self._heap) - 1:
            return 2 * parent_idx + 1
        if self._heap[2 * parent_idx + 1] < self._heap[2 * parent_idx + 2]:
            return 2 * parent_idx + 1
        return 2 * parent_idx + 2

    def insert(self, item: Any):
        """Add a new item"""
        self._heap.append(item)
        self.perc_up(len(self._heap) - 1)

    def delete(self) -> Any:
        """Remove an item from the heap"""
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        result = self._heap.pop()
        self.perc_down(0)
        return result

    def heapify(self, not_a_heap: List[Any]) -> None:
        """Turn a list into a heap"""
        self._heap = not_a_heap[:]
        cur_idx = len(self._heap) // 2 - 1
        print(cur_idx)
        while cur_idx >= 0:
            print(self)
            self.perc_down(cur_idx)
            cur_idx = cur_idx - 1

    def __len__(self) -> int:
        """Get heap size"""
        return self._size

    def __str__(self) -> str:
        """Heap as a string """
        return str(self._heap)


class BinaryHeapMax:
    """Heap class implementation"""
    def __init__(self):
        """Initializer"""
        self._heap: List[Any] = []
        self._size = 0

    def perc_up(self, cur_idx: int):
        """Move a node up"""
        while (cur_idx - 1) // 2 >= 0:
            parent_idx = (cur_idx - 1) // 2
            if self._heap[cur_idx] > self._heap[parent_idx]:
                self._heap[cur_idx], self._heap[parent_idx] = (
                    self._heap[parent_idx],
                    self._heap[cur_idx],
                )
            cur_idx = parent_idx

    def perc_down(self, cur_idx: int):
        """Move a node down"""
        while 2 * cur_idx + 1 < len(self._heap):
            min_child_idx = self._get_min_child(cur_idx)
            if self._heap[cur_idx] > self._heap[min_child_idx]:
                self._heap[cur_idx], self._heap[min_child_idx] = (
                    self._heap[min_child_idx],
                    self._heap[cur_idx],
                )
            else:
                return
            cur_idx = min_child_idx

    def _get_min_child(self, parent_idx):
        if 2 * parent_idx + 2 > len(self._heap) - 1:
            return 2 * parent_idx + 1
        if self._heap[2 * parent_idx + 1] < self._heap[2 * parent_idx + 2]:
            return 2 * parent_idx + 1
        return 2 * parent_idx + 2

    def insert(self, item: Any):
        """Add a new item"""
        self._heap.append(item)
        self.perc_up(len(self._heap) - 1)

    def delete(self) -> Any:
        """Remove an item from the heap"""
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        result = self._heap.pop()
        self.perc_down(0)
        return result

    def heapify(self, not_a_heap: List[Any]) -> None:
        """Turn a list into a heap"""
        self._heap = not_a_heap[:]
        cur_idx = len(self._heap) // 2 - 1
        while cur_idx >= 0:
            print(self)
            self.perc_down(cur_idx)
            cur_idx -= 1

    def __len__(self) -> int:
        """Get heap size"""
        return self._size

    def __str__(self) -> str:
        """Heap as a string """
        return str(self._heap)


def main():
    """Main"""
    heap = BinaryHeapMax()
    # heap.heapify([-69, -10, -28, -7, -89, -83, -41, -17, -73, -55])
    # heap.heapify([69, 10, 28, 7, 89, 83, 41, 17, 73, 55])
    heap.insert(55)
    heap.insert(73)
    heap.insert(17)
    heap.insert(41)
    heap.insert(83)
    heap.insert(89)
    heap.insert(7)
    heap.insert(28)
    heap.insert(10)
    heap.insert(69)
    print(heap)

    # a_heap = BinaryHeapMin()
    # a_heap.heapify([9, 5, 6, 2, 3])
    # b_heap = BinaryHeapMin()
    # b_heap.heapify([55, 73, 17, 41, 83, 89, 7, 28, 10, 69])
    # c_heap = BinaryHeapMin()
    # c_heap.heapify([42, 35, 71, 34, 76, 39, 77, 47, 6, 20])
    # print(a_heap)
    # print(b_heap)
    # print(c_heap)


if __name__ == "__main__":
    main()
