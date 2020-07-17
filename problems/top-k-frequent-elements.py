# Heap: O(n*log(k)) time and O(n) space

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
    
    
    
# Bucket sort: O(n) time and O(n^2) space (in worst case)

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        count = Counter(nums).items()  
        for num, freq in count: 
            buckets[freq].append(num) 
        flat_list = [item for bucket in buckets for item in bucket]
        return flat_list[::-1][:k]
