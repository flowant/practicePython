"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        138. Copy List with Random Pointer
        https://leetcode.com/problems/copy-list-with-random-pointer/description/

        Except for random pointers, we can copy linked list.

        # can be made during the copy of list
        input_ref_index_map (input sequence is keepd since python 3.7 or 3.8?)
        {
            # reference: index
            ...
            None: None
        }

        # can be made during the copy of list
        output_index_ref_map
        {
            # index: reference
            None: None
        }

        output list
        val and next nodes are filled during the copy

        #throught new linked list
        i
            random_index = input_ref_index_map[org_node.random]
            new_random_ref = output_index_ref_map[random_index]

        Time, space complexity = O(2n)
        """

        if not head:
            return None

        input_ref_index_map = {None: None}
        output_index_ref_map = {None: None}

        cur_node = head

        new_head = None
        new_prev_node = None

        # head = [cn0[1,1], cn1[2,1]]
        i = 0
        while cur_node:  # cn0, cn1, None
            new_node = Node(cur_node.val)  # nn0, nn1
            if new_head is None:
                new_head = new_node  # nn0
            if new_prev_node is not None:
                new_prev_node.next = new_node  ## nn0.next = nn1
            input_ref_index_map[cur_node] = i  # cn0: 0, cn1: 1
            output_index_ref_map[i] = new_node  # 0: nn0, 1: nn1

            new_prev_node = new_node  # nn0, nn1
            cur_node = cur_node.next
            i += 1

        # new_head = [nn0[1,None], nn1[2,None]]

        cur_node = head
        new_cur_node = new_head
        i = 0
        while cur_node:  # cn0, cn1
            random_index = input_ref_index_map[cur_node.random]  # 1, 1
            new_random_ref = output_index_ref_map[random_index]  # nn1, nn1
            new_cur_node.random = new_random_ref  # nn1

            cur_node = cur_node.next
            new_cur_node = new_cur_node.next
            i += 1

        return new_head
