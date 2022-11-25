class Solution:

    UNVISITED = 0
    VISITED = 1
    VISITED_AND_CYCLE_NOT_FOUND = 2

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        210. Course Schedule II
        https://leetcode.com/problems/course-schedule-ii/description/

        Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
        Output: [0,2,1,3]

        DFS
        visit_status: UNVISITED, VISITED, VISITED_AND_CYCLE_NOT_FOUND
        path_stack: add the last node first before unwinding call stack

        0 V > 1 VCNF > 3 VCNF
         |- > 2 V  -^

        0 V > 2 VCNF > 3 VCNF > 4 VCNF

        [4, 3, 2, 0]

        0 V > 1 V > 3 V > 0 V
        """
        if not numCourses:
            return []

        graph = defaultdict(list)
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        is_cycle_found = False
        visit_status = [Solution.UNVISITED for i in range(numCourses)]
        path_stack = list()

        def dfs(course, start_course):  # 0, 1 3
            nonlocal is_cycle_found
            if is_cycle_found:
                return

            visit_status[course] = Solution.VISITED

            for next_course in graph[course]:  # 3
                if visit_status[next_course] == Solution.VISITED:
                    is_cycle_found = True
                    return
                if visit_status[next_course] == Solution.UNVISITED:
                    dfs(next_course, start_course)

            # remove visit marks during unwinding call stack
            visit_status[course] = Solution.VISITED_AND_CYCLE_NOT_FOUND
            path_stack.append(course)

        for course in range(numCourses):  # 0
            if is_cycle_found:
                return []
            if visit_status[course] == Solution.UNVISITED:
                dfs(course, course)

        return reversed(path_stack)
