from collections import defaultdict, Counter
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        out, graph = [0]*n, defaultdict(set)
        for a, b in edges: graph[a].add(b); graph[b].add(a)    
        
        def dfs(node):
            counts = Counter([labels[node]])
            for child in graph[node]:
                graph[child].discard(node)
                counts += dfs(child)
            out[node] = counts[labels[node]]
            return counts
        
        dfs(0)
        return out
