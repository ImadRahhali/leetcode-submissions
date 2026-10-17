class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        preMap = {i : [] for i in range(n)}
        for src, dist in prerequisites:
            preMap[src].append(dist)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if preMap[course] == []:
                return True
            visited.add(course)
            for neighbour in preMap[course]:
                if not dfs(neighbour):
                    return False
            visited.remove(course)
            preMap[course] = []
            return True
    
        for course in range(n):
            if not dfs(course):
                return False
        return True