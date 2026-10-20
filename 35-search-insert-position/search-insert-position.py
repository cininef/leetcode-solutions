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
        #不管target在还是不在，l都是第一个大于或等于 target 的位置 -> 插入点
        return l