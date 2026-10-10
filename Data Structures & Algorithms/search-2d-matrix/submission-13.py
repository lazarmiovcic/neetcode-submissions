class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = 0, len(matrix[0]) - 1
        lr, rr = 0, len(matrix) - 1
        while lr <= rr:
            mid = lr + (rr - lr) // 2
            if matrix[mid][c] < target:
                lr = mid + 1
            elif matrix[mid][c] > target:
                rr = mid - 1
            else:
                return True
        r = lr

        if r >= len(matrix):
            return False

        lc, rc = 0, len(matrix[0]) - 1
        while lc <= rc:
            mid = lc + (rc- lc) // 2
            if matrix[r][mid] < target:
                lc = mid + 1
            elif matrix[r][mid] > target:
                rc = mid - 1
            else:
                return True
        c = lc
        return False