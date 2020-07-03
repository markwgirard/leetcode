class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        h = {}
        day = 0
        while N:
            if str(cells) in h:
                cycle_length = day - h[str(cells)]
                return self.prisonAfterNDays(cells, N % cycle_length)
            h[str(cells)] = day
            N -= 1
            day += 1
            cells = self.NextPrisonDay(cells)
        return cells
    
    def NextPrisonDay(self, cells):
        next_cells = [0]*len(cells)
        for i in range(1, len(cells) - 1):
            next_cells[i] = int(cells[i-1]==cells[i+1])
        return next_cells
