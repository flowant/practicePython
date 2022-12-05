class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        1029. Two City Scheduling

        Input: costs = [[10,20],[30,200],[400,50],[30,20]]
        Output: 110

                                     savings
                                 a - b    b - a
        1: [(a, 10), (b, 20)],   -10      10
        2: [(a, 30), (b, 200)],  -170     170
        3: [(a, 400), (b, 50)],  350      -350
        4: [(a, 30), (b, 20)],   10       -10

        # Time complexity of sort is O(nLogn)
        # Space complexsity is about O(logN), it depends on the implementation

        """
        if not costs:
            return 0

        costs.sort(key=lambda x: x[0] - x[1])

        len_half = len(costs) // 2
        result = 0

        for i in range(len_half):
            result += costs[i][0]  # i 0 1
            result += costs[i + len_half][1]  # i + len_half 2 3

        return result
