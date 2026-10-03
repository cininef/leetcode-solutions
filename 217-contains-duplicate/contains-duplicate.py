class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = set(nums)
        if len(nums)!= len(n):
            return True
        return False