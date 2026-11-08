class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        rotten = set()

        q = deque([])


        fresh_count = 0

        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    q.append((i, j, 0))
        
        if not fresh_count:
            return 0
        

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r, c, minutes = q.popleft()

            for rd, cd in directions:
                row, col = r + rd, c + cd

                if row in range(N) and col in range(M):
                    if grid[row][col] == 1 and (row, col) not in rotten:
                        q.append((row,col,minutes + 1))
                        rotten.add((row,col))
                        fresh_count -= 1

        return minutes if fresh_count == 0 else -1