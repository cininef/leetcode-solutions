class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #method 1: brute force, use sort
        sn = sorted(nums)
        n = len(nums)
        return sn[n-k]