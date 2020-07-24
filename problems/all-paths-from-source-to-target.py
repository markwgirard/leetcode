from collections import defaultdict
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        graphTr =  defaultdict(set)
        for i in range(n):
            for j in graph[i]:
                graphTr[j].add(i)

        def removeDeadEnds(v):
            if v == 0 : return False
            for u in graphTr[v]:
                if removeDeadEnds(u): 
                    graphTr[v].discard(u)
            return not graphTr[v]

        removeDeadEnds(n-1)            
        
        paths = defaultdict(list)
        paths[0] = [[]]
        
        stack = [0]
        while stack:
            i = stack.pop()
            paths[i] = [path+[i] for path in paths[i]]
            if i == n-1: break
            for j in graph[i]:
                paths[j].extend(paths[i])
                graphTr[j].discard(i)
                if not graphTr[j]:
                    stack.append(j)
            del paths[i]        
        
        return paths[n-1]
