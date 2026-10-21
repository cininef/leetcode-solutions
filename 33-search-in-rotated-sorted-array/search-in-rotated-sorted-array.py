class Solution:
    def search(self, nums: list[int], target: int) -> int:
        #拆分法：先跟153一样找到变化点
        #unique+bs search target not boundary
        def find_min_idx():
            l,h = 0,len(nums)-1
            while l<h:
                m = (l+h)//2
                if nums[m]<=nums[-1]:
                    h = m
                else:
                    l = m+1
            return l
        min_idx = find_min_idx()
        high = nums[0:min_idx]
        low = nums[min_idx:]
        def bs_target(nums):
            l,h = 0,len(nums)
            while l<h:
                m = (l+h)//2
                if target<=nums[m]:
                    h = m
                else:
                    l = m+1
            return l if l<len(nums) and nums[l]==target else -1

        if target <= low[-1]:
            return bs_target(low)+min_idx if bs_target(low)!=-1 else -1
        else:
            return bs_target(high)

        

        