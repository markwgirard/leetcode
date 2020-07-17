from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1

        hp = [(-freqs[num], num) for num in freqs]
        heapq.heapify(hp)
        return [heapq.heappop(hp)[1] for _ in range(k)]
