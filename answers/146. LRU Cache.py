from collections import OrderedDict


class LRUCache:
    """
    146. LRU Cache
    https://leetcode.com/problems/lru-cache/description/

    Space complexity: N, N is the capacity
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.od = OrderedDict()

    def get(self, key: int) -> int:
        """
        Time complexity: O(1)
        """
        if key in self.od:
            self.od.move_to_end(key)
            return self.od[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        """
        Time complexity: O(1)
        """
        if key in self.od:
            self.od.move_to_end(key)
        elif len(self.od) == self.capacity:
            self.od.popitem(last=False)
        self.od[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
