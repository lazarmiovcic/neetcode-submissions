class Solution: 
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = l + (r-l) // 2
            val = matrix[mid // m][mid % m]
            if val == target:
                return True
            elif val < target:
                l=mid+1
            else:
                r = mid - 1
        return False
    