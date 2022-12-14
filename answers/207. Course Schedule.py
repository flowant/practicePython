class Solution:
    UNVISITED = 0
    VISITED = 1
    VISITED_AND_CYCLE_NOT_FOUND = 2

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        207. Course Schedule
        https://leetcode.com/problems/course-schedule/description/

        Input: numCourses = 3, prerequisites = [[2,1],[1,0],[0, 2]]
        Output: false

        Input: numCourses = 3, prerequisites = [[1,0],[2,0],[2, 1]]
        Output: True

        Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
        Output: false

        DFS(node, start_node), if start_node is re-visited, cycle is found and then return False
        len(visited) == numCourses then return true

        Time, space complexity = O(E + V)

        """

        if not numCourses:
            return False

        graph = defaultdict(list)
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        is_cycle_found = False
        visit_status = [Solution.UNVISITED for i in range(numCourses)]

        def dfs(course, start_course):  # 0, 1 3
            nonlocal is_cycle_found
            if is_cycle_found:
                return

            visit_status[course] = Solution.VISITED

            for next_course in graph[course]:  # 3
                if visit_status[next_course] == Solution.VISITED:
                    is_cycle_found = True
                    return
                if visit_status[next_course] in (Solution.UNVISITED,):
                    dfs(next_course, start_course)

            # remove visit marks during unwinding call stack
            visit_status[course] = Solution.VISITED_AND_CYCLE_NOT_FOUND

        for course in list(graph.keys()):  # 0
            if is_cycle_found:
                return False
            if visit_status[course] == Solution.UNVISITED:
                dfs(course, course)

        return True
