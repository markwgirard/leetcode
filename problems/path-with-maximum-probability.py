import collections
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        neighbours = collections.defaultdict(list)
        for (i, j), p in zip(edges,succProb):
            neighbours[i].append((j,p))
            neighbours[j].append((i,p))
        maxProbs = [0]*n
        maxProbs[start] = 1
        q = collections.deque([start])
        while q:
            node = q.popleft()
            prob = maxProbs[node]
            if prob < maxProbs[end]: continue
            for neighbour, travProb in neighbours[node]:
                newProb = prob*travProb
                if newProb > maxProbs[neighbour]:
                    maxProbs[neighbour] = newProb
                    q.append(neighbour)
        return maxProbs[end]
