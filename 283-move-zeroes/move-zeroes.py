class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #快慢指针 同向：核心 inplace更改list
        slow = 0
        for fast in range(len(nums)):
            #the element want to preserve and put front
            if nums[fast]!=0:
                nums[slow] = nums[fast]
                slow += 1
        for i in range(slow,len(nums)):
            nums[i]=0

'''
fast=读：扫描每一个元素	每轮都 +1
slow=写：下一个保留元素放在哪的空位，只有当 fast 找到了合格的元素交换fastslow现在的元素 才+1下一个
def fast_slow(nums):
    slow = 0                          # slow：下一个"要保留的元素"写到哪里
    for fast in range(len(nums)):     # fast：逐个扫描每个元素
        if 满足保留条件(nums[fast]):
            nums[slow], nums[fast] = nums[fast], nums[slow]   # 或者 nums[slow] = nums[fast]
            slow += 1
    return slow                       # [0, slow) 就是处理好的结果
'''   