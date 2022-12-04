class OrderedStream:
    """
    1656. Design an Ordered Stream

    Input
    ["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
    [[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]

    Output
    [null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]
    """

    def __init__(self, n: int):
        self._len_stream = n
        self._stream = [None] * n
        self._next_index = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self._stream[idKey - 1] = value
        # 0 1 2 3 4
        # a b c d e
        for i in range(self._next_index, self._len_stream + 1): # 3 4 5
            if i == self._len_stream or self._stream[i] == None:
                result = self._stream[self._next_index:i] # [3:5]
                self._next_index = i # 1 3
                return result

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
