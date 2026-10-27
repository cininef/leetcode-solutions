class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        #快慢指针：inplace修改array=把不想要的弄后面/空
        slow = 0
        count = 0
        for fast in range(len(nums)):
            if nums[fast]!=val:
                nums[slow],nums[fast] = nums[fast],nums[slow]
                count += 1
                slow += 1
        return count