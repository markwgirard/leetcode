class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    neighbours = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
                    for (a, b) in neighbours:
                        if not (0 <= a < m and 0 <= b < n) or not grid[a][b]:
                            count += 1
        return count
