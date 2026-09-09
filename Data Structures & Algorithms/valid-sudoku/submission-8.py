class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for i in range(9):
            nums = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in nums:
                    return False
                nums.add(board[i][j])

        # Check columns
        for i in range(9):
            nums = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in nums:
                    return False
                nums.add(board[j][i])

        # Check 3x3 boxes
        ls = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                box = (i // 3) * 3 + j // 3

                if board[i][j] in ls[box]:
                    return False

                ls[box].add(board[i][j])

        return True
