class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #暴力拆解
        
        for i,num1 in enumerate(nums):
            for j in range(i+1,len(nums)):
                if num1+nums[j] == target:
                    return [i,j]
        