class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        #ascending/duplicates
        slow = 0
        for fast in range(len(nums)):
            #cases1:no duplicate, new elements ->fast!=slow-1
            #case2:duplicate with slow-1, but not slow-2
            #case3:initial, slow==0
            if (
                (nums[fast]!=nums[slow-1]) or 
                (slow == 0 or slow == 1) or
                (nums[fast]==nums[slow-1] and nums[fast]!=nums[slow-2])
                
            ):
                nums[slow] = nums[fast]
                slow += 1
        return slow

