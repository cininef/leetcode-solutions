class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #hashmap:变成表 因为要返回value index有两个变量
        dict = {}
        for i in range(len(nums)):
            #define the num2 going to find
            num2 = target - nums[i]
            if num2 in dict:
                return [i,dict[num2]]
            dict[nums[i]] = i


        