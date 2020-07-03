class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = {} # hash map of most recent position of each character that has appeared
        start = longest = 0
        for i, char in enumerate(s):
            if char in h: 
                start = max(start, h[char] + 1)
            h[char] = i
            longest = max(longest, i - start + 1)
        return longest
