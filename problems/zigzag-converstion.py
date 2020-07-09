class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows<=1: return s
        ans = ['']*numRows
        row, direction = 0, 'down'
        for char in s:
            ans[row if direction == 'down' else -1*(row+1)] += char
            if row == numRows - 2:
                direction = 'up' if direction == 'down' else 'down'
            row = (row + 1)%(numRows-1)
        return ''.join(ans)
