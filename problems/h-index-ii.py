class Solution:
    def hIndex(self, citations: List[int], naive = False) -> int:
        # "Naive" method sorts the citations then uses binary search
        if naive:
            citations.sort(reverse=True)
            l, r = 0, len(citations)-1
            while l <= r:
                m = (l+r)//2
                if citations[m] <= m:
                    r = m - 1
                else:
                    l = m + 1
            return l
            
        # This method is O(n) time and O(1000) space
        bins = [0]*1000
        for i in citations:
            bins[i]+=1
        h = 0
        for i in range(999,-1,-1):
            while bins[i]:
                if h < i:
                    bins[i]-=1
                    h+=1
                else:
                    return h
        return h
