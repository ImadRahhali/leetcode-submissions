class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        preMap = {i: [] for i in range(n)} 
        for a, b in prerequisites:
            preMap[a].append(b)
        
        path = set()
        visited = set()
        res = []
        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True
            
            path.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            path.remove(course)
            visited.add(course)
            res.append(course)
            return True
        
        for course in range(n):
            if not dfs(course):
                return []
        return res