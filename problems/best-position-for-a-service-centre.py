# One-liner using scipy
import numpy as np
from scipy.optimize import minimize
class Solution(object):
    def getMinDistSum(self, positions):
        return minimize(lambda p: np.sum(np.sqrt(np.sum(np.square(p - positions), axis=1))), np.zeros(2)).fun

# my first attempt with grad descent
import math
import numpy as np

class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        self.positions = np.array(positions)
        self.n = len(positions)
        xy = np.sum(self.positions, axis = 0) / self.n
        
        alpha = 1
        dec = float('inf')
        val = self.dist(xy)
        eps = 10**(-6)
        stepNum = 0
        
        while dec > 10**(-10) and stepNum <1000:
            xyLast = xy
            xy = xy - alpha*self.grad(xy)
            while self.dist(xy) > val:
                xy = (xy + xyLast) / 2
            valLast, val = val, self.dist(xy)
            dec = valLast - val
            stepNum += 1
        return val
    
    
    def helper(self, xy):
        diffs = np.zeros((self.n, 2))
        diffs[:,0] = xy[0] - self.positions[:,0]
        diffs[:,1] = xy[1] - self.positions[:,1]
        distsSqr = diffs[:,0]**2 + diffs[:,1]**2
        return diffs, distsSqr
    
    def grad(self, xy):
        diffs, dists = self.helper(xy)
        g = np.zeros(2)
        g[0] = np.sum(diffs[:,0]/np.sqrt(dists))
        g[1] = np.sum(diffs[:,1]/np.sqrt(dists))
        return np.nan_to_num(g)
    
    def dist(self, xy):
        diffs, distsSqr = self.helper(xy)
        return np.sum(np.sqrt(distsSqr))
