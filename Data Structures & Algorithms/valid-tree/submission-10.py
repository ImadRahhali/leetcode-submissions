class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(n)}
        for src, dist in edges:
            adjList[src].append(dist)
            adjList[dist].append(src)
        visited = set()
        visited.add(0)
        queue = deque()
        queue.append([0, -1])

        while queue:
            curr, parent = queue.popleft()
            for child in adjList[curr]:
                if child == parent:
                    continue
                if child in visited:
                    return False
                visited.add(child)
                queue.append([child, curr])
        return len(visited) == n
                
