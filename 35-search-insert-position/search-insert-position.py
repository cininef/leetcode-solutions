class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l,h = 0,len(nums)
        while l<h:
            m = (l+h)//2
            # means on [l,m] interval
            if target <= nums[m]:
                h = m
            else:
                l = m+1
        return l