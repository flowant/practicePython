class Solution:

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        399. Evaluate Division
        https://leetcode.com/problems/evaluate-division/description/

        Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0],
               queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
        Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]

        - Use DFS

        [["a","b"],["b","c"]], values = [2.0,3.0],
        [["b","a"],["c","b"]], values = [1/2.0,1/3.0],

        - Build Graph
        graph = {
            a: {
                b: 2.0
            }
            b: {
                c: 3.0,
                a: 1/2.0,
            }
            c: {
                b: 1/3.0
            }
        }

        queries
        a -> b -> c
        a/b * b/c = a/c
        2.0 * 3.0 = 6

        Time Complexity: O(QE), E is the length of the equations, Q is the length of the Queries.
        Space complexity: O(2E)
        """

        if not equations or not values or len(equations) != len(values) or not queries:
            return []

        graph = defaultdict(defaultdict)

        for i in range(len(equations)):
            dividend, divisor = equations[i]  # a b |
            value = values[i]  # 2.0
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value

        # Constants of visit_status
        UNVISITED = 0
        VISITED = 1
        VISITED_BACKTRACKED = 2

        def dfs(node, end_node, visit_status, acc_value=1):  # b a, )
            nonlocal answer  # None
            visit_status[node] = VISITED  # { b: VISITED_BACKTRACKED, }

            for next_node, next_value in graph[node].items():
                if answer is not None:
                    return
                if visit_status[next_node] == UNVISITED:
                    if next_node == end_node:
                        answer = acc_value * next_value
                    else:
                        dfs(next_node, end_node, visit_status, acc_value * next_value)

            visit_status[node] = VISITED_BACKTRACKED

        # queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
        answers = list()
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                answers.append(-1.0)
            elif dividend == divisor:
                answers.append(1.0)
            else:
                visit_status = defaultdict(lambda: UNVISITED)
                answer = None
                dfs(dividend, divisor, visit_status)
                answers.append(answer if answer is not None else -1.0)

        return answers
