class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        #m2 two pointer 快慢指针
        slow = 0
        ns = set()
        for fast in range(len(nums)):
            if nums[fast] not in ns:
                ns.add(nums[fast])
                nums[slow],nums[fast] = nums[fast],nums[slow]
                slow += 1
        return len(ns)
