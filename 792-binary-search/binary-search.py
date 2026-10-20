class Solution:
    def search(self, nums: list[int], target: int) -> int:
        #返回bs 是否找到 最大index就在n-1 不会超过
        l,h = 0, len(nums)-1
        while l < h:
            m = (l+h)//2
            #target on the [l,m]
            if target <= nums[m]:
                h = m
            else:
                l = m+1
        # remember to consider not exist: lmh三点归一 都找不到
        return l if target == nums[l] else -1
