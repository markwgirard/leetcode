class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return False
        m, n = len(board), len(board[0])
        
        def search(i, j, word, used):
            if not word:
                return True
            if not (0<=i<m and 0<=j<n) or board[i][j] != word[0] or (i,j) in used: 
                return False
            for a,b in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                if search(a,b,word[1:],used.union([(i,j)])):
                    return True
            return False
 
        for i in range(m):
            for j in range(n):
                if search(i,j,word,set()):
                    return True
        return False
