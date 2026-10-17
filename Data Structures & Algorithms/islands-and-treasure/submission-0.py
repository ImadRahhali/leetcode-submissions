class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append((i,j))
        length = 0
        while queue:
            length += 1
            for i in range(len(queue)):
                r,c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 2147483647):
                            grid[nr][nc] = length
                            queue.append((nr,nc))
                