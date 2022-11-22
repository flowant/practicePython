# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        23. Merge k Sorted Lists
        https://leetcode.com/problems/merge-k-sorted-lists/description/

        Brute Force:
        - add all node to list O(n)
        - sort the list O(nlogn)
        [
           a, 1->4->5,
           b, 1->3->4,
           c, 2->6
        ]

        min heap [a.1, b.1, c.2]

        (1, node.next)
        if node.next is not None:
            push to the next node to heap
        """
        # To compare only the first value of tuple in heap
        ListNode.__lt__ = lambda self, x: False

        if not lists or all([not bool(e) for e in lists]):
            return None

        min_heap = [(node.val, node) for node in lists if node]
        heapq.heapify(min_heap)

        result_head = None
        result_tail = None
        while len(min_heap) > 0:
            min, min_node = heapq.heappop(min_heap)

            temp = ListNode(min)

            if result_head is None:
                result_head = temp

            if result_tail is not None:
                result_tail.next = temp
            result_tail = temp

            if min_node.next is not None:
                next_node = min_node.next
                heapq.heappush(min_heap, (next_node.val, next_node))

        return result_head  # a.1 b.1 c.2 b.3 a.4 b.4 a.5 c.6
