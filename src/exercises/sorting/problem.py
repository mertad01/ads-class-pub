#!/usr/bin/env python3
"""Working File"""

# a_list = [15, 16, 73, 65, 38, 10, 22, 79, 87, 64]

# class BinaryHeap:
#     def __init__(self):
#         self._heap = []

#     def _perc_up(self, cur_idx):
#         while (cur_idx - 1) // 2 >= 0:
#             parent_idx = (cur_idx - 1) // 2
#             if self._heap[cur_idx] < self._heap[parent_idx]:
#                 self._heap[cur_idx], self._heap[parent_idx] = (
#                     self._heap[parent_idx],
#                     self._heap[cur_idx],
#                 )
#             cur_idx = parent_idx

#     def _perc_down(self, cur_idx):
#         while 2 * cur_idx + 1 < len(self._heap):
#             min_child_idx = self._get_min_child(cur_idx)
#             if self._heap[cur_idx] > self._heap[min_child_idx]:
#                 self._heap[cur_idx], self._heap[min_child_idx] = (
#                     self._heap[min_child_idx],
#                     self._heap[cur_idx],
#                 )
#             else:
#                 return
#             cur_idx = min_child_idx

#     def _get_min_child(self, parent_idx):
#         if 2 * parent_idx + 2 > len(self._heap) - 1:
#             return 2 * parent_idx + 1
#         if self._heap[2 * parent_idx + 1] < self._heap[2 * parent_idx + 2]:
#             return 2 * parent_idx + 1
#         return 2 * parent_idx + 2

#     def heapify(self, not_a_heap):
#         self._heap = not_a_heap[:]
#         cur_idx = len(self._heap) // 2 - 1
#         while cur_idx >= 0:
#             self._perc_down(cur_idx)
#             print(self._heap)
#             cur_idx = cur_idx - 1

#     def get_min(self):
#         return self._heap[0]

#     def insert(self, item):
#         self._heap.append(item)
#         self._perc_up(len(self._heap) - 1)

#     def delete(self):
#         self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
#         result = self._heap.pop()
#         self._perc_down(0)
#         return result

#     def is_empty(self):
#         return not bool(self._heap)

#     def __len__(self):
#         return len(self._heap)

#     def __str__(self):
#         return str(self._heap)

# a_heap = BinaryHeap()
# a_heap.heapify([15, 16, 73, 65, 38, 10, 22, 79, 87, 64])
# print(a_heap)

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        print(arr)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)

# Driver code to test above
arr = [15, 16, 73, 65, 38, 10, 22, 79, 87, 64]
heapSort(arr)
n = len(arr)
print(arr)
# for i in range(n):
#     print ("%d" %arr[i]),
