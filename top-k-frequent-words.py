from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = defaultdict(int)
        for word in words:
            freq[word] += 1
        
        # Make a heap of the words ordered by frequency then alphabetically.
        # If heap is longer than k, pop smallest element.
        heap = []
        for word, count in freq.items():
            heapq.heappush(heap, Item(count, word))
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Pop elements from smallest to largest, then reverse the output.
        return reversed([heapq.heappop(heap).word for _ in range(k)])
    
    
class Item(object):
    ```
    Make an object with attributes word and count. Order is determined by count, followed by alphabetical order of words.
    ```
    def __init__(self, count, word):
        self.count = count
        self.word = word
    
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count
