class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        #m2 two pointer 快慢指针
        slow = 0
        for fast in range(slow,len(nums)):
            #slow it's the current to replace
            #slow-1 it's the last unique element
            #fast to find next unique elements
            if slow==0 or nums[fast]!=nums[slow-1]:
                nums[slow]= nums[fast]
                slow += 1
        return slow
'''
1.不在意，题目只看前 k 个
-> 覆盖 nums[slow] = nums[fast]	26、27、80
2.在意，题目要求后面也正确	swap 
->nums[slow],nums[fast] = nums[fast],nums[slow] 	
283（后面必须全是 0）
'''
