class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visited = set()

        def bfs(i, j):
            q = deque([(i, j)])

            directions = [(1,0), (-1,0), (0, 1), (0,-1)]
            while q:
                r, c = q.popleft()

                for rd, cd in directions:
                    row, col = r - rd, c - cd
                    if row in range(len(grid)) and col in range(len(grid[0])):
                        if grid[row][col] == "1" and (row, col) not in visited:
                            q.append((row,col))
                            visited.add((row,col))
                    

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    res += 1
        return res
