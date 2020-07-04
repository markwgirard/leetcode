#import sys

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi)//2
            j = (m + n)//2 - i
            L1 = nums1[i-1] if i > 0 else -1000000#-sys.maxsize #float('-inf')
            L2 = nums2[j-1] if j > 0 else -1000000#-sys.maxsize #float('-inf')
            R1 = nums1[i] if i < m else 1000000#sys.maxsize #float('inf')
            R2 = nums2[j] if j < n else 1000000#sys.maxsize #float('inf')
            if L1 <= R2 and L2 <= R1:
                if (m+n)%2:
                    return min(R1,R2)
                return (max(L1,L2) + min(R1,R2))/2
            if L1 > R2:
                hi = i - 1
            if L2 > R1:
                lo = i + 1
        
        return 0
