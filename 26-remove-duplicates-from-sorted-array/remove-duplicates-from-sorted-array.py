class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        #m1 brute force
        #set won't preserve the original sequence in list  
        uniq_nums = sorted(set(nums))
        #must use slicing, replace nums = uniq_nums only change a reference/pointer to nums, but every element stays the same
        nums[:] = uniq_nums
        return len(uniq_nums)