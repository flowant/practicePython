"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        430. Flatten a Multilevel Doubly Linked List

        while loop:
        When node has child
        node.child.prev = node

        call flatten recursively
        return the right most node of the child
        if node.next:
            node.next.prev = last_child_node
        last_node.next = node.next
        node.next = node.child
        node.child = None

        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        if not head:
            return head

        def _flatten(node):
            last_sibiling_node = None
            while node:  # 3
                if node.child:
                    node.child.prev = node  # 7.prev = 3
                    last_child_node = _flatten(node.child)  # 10
                    if node.next:
                        node.next.prev = last_child_node
                    last_child_node.next = node.next  # 10.next = 4
                    node.next = node.child  # 3.next = 7
                    node.child = None

                last_sibiling_node = node  # 1 3
                node = node.next  # 2

            return last_sibiling_node

        _flatten(head)
        return head
