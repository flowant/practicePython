class Solution:
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
        visited_and_cycle_not_found = set()

        def dfs(course, start_course, visited):  # 0, 1 3
            nonlocal is_cycle_found
            if is_cycle_found:
                return

            visited_and_cycle_not_found.add(course)
            visited.add(course)  # 4 2 1

            for next_course in graph[course]:  # 3
                if next_course in visited:
                    is_cycle_found = True
                    return
                if next_course not in visited and next_course not in visited_and_cycle_not_found:
                    dfs(next_course, start_course, visited)

            # remove visit marks during unwinding call stack
            visited.remove(course)

        for course in list(graph.keys()):  # 0
            if is_cycle_found:
                return False
            if course not in visited_and_cycle_not_found:
                dfs(course, course, set())

        return True
