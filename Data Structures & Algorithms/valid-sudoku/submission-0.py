class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                
                row_key = ('row', r, val)
                col_key = ('col', c, val)
                box_key = ('box', r//3, c//3, val)

                if row_key in seen or col_key in seen or box_key in seen:
                    return False
                
                seen.update([row_key, col_key, box_key])
        
        return True