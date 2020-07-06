from math import gcd
from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3: return len(points)
        max_count = 0
        lines = defaultdict(lambda : 0)
        for i in range(len(points)):
            x1, y1 = points[i]
            lines[x1] = 0
            num_copies = 1
            for j in range(i+1,len(points)):
                x2, y2 = points[j]
                if (x1,y1) == (x2,y2):
                    num_copies += 1
                else:
                    lines[LineIdentifierFromPoints(x1,y1,x2,y2)] += 1
                
            max_count = max(max_count, max(lines.values()) + num_copies)
            lines.clear()
        return max_count
                
def LineIdentifierFromPoints(x1,y1,x2,y2):
    """
    Return slope/y-intercept pair (m,b) for two points (x1,y1) and (x2,y2).
    If slope is infinite, return x where x is x-intercept.
    """
    if x1 == x2: return x1
    if x1 > x2: return LineIdentifierFromPoints(x2,y2,x1,y1)
    deltax, deltay, cross = (x2 - x1), (y2 - y1), (x1*y2 - x2*y1)
    m = MakeFraction(deltay,deltax)
    b = MakeFraction(cross,deltax)
    return (m,b)

def MakeFraction(m,n):
    if n == 0: return (0,0)
    g = gcd(m,n)
    return (m//g, n//g)
