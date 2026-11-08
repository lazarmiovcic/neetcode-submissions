class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        visited = set()
        res = 0

        def bfs(i, j):
            q = deque([(i, j)])
            area = 1
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            while q:
                r, c = q.popleft()
                for rd, cd in directions:
                    row, col = r - rd, c - cd
                    if row in range(N) and col in range(M) and grid[row][col] == 1 and (row, col) not in visited:
                        q.append((row, col))
                        visited.add((row,col))
                        area += 1
            return area

        for r in range(N):
            for c in range(M):
                if (r,c) not in visited and grid[r][c] == 1:
                    visited.add((r,c))
                    area = bfs(r,c)
                    res = max(res, area)
        return res
                