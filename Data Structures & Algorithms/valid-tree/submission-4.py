class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(n)}
        for src, dist in edges:
            adjList[src].append(dist)
            adjList[dist].append(src)
        visited = set()
        queue = deque()
        queue.append([0, -1])

        while queue:
            for i in range(len(queue)):
                curr, parent = queue.popleft()
                if curr in visited:
                    return False
                visited.add(curr)
                for child in adjList[curr]:
                    if child != parent:
                        queue.append([child, curr])
        return len(visited) == n
                
