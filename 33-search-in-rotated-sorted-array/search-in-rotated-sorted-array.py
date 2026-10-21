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
        #slicing复制 不符合要求了 不满足logN
        def bs_target(l,h):

            while l<h:
                m = (l+h)//2
                if target<=nums[m]:
                    h = m
                else:
                    l = m+1
            return l if l<len(nums) and nums[l]==target else -1

        if target <= nums[-1]:
            return bs_target(min_idx,len(nums)-1)
        else:
            return bs_target(0,min_idx-1)

        

        