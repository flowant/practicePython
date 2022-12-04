from random import choice


class RandomizedSet:
    """
    380. Insert Delete GetRandom O(1)

    """

    def __init__(self):
        self.map_value_index = dict()
        self.list_value = list()

    def insert(self, val: int) -> bool:
        """
        {
            10: 0,
            11: 1
        }

        i
        [10, 11]
        """
        if val not in self.map_value_index:
            self.list_value.append(val)
            self.map_value_index[val] = len(self.list_value) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        swap the last element and the val element before deletion
        delete the last element
        {
            10: 0,
            11: 1
        }

        i
        [10, 11]
        """
        if val in self.map_value_index:  # 10
            index_of_value = self.map_value_index[val]  # 0
            last_value = self.list_value[-1]  # 11
            self.list_value[index_of_value] = last_value  # [11]
            self.map_value_index[last_value] = index_of_value
            self.list_value.pop()
            del self.map_value_index[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return choice(self.list_value)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()