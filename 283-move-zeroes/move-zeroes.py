class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #快慢指针 同向：核心 inplace更改list
        slow = 0
        #fast只走一次全局 更新在上次slow+=1应该改变的位置 对于把slow上面元素直接改变的事情 
        '''fast>=slow
        if fast == slow: 直接原地交换互换 所以这就是不能直接把fast=0的原因 有可能前面没有一个0元素 所以fast==slow
        if fast>slow: 现在slow的元素之前本来也被放到slow以前的位置了 所以 slow-fast之间的元素 都是0 把slow换到fast就把0往后移动了
        [ 0 ... slow-1 ]  [ slow ... fast-1 ]  [ fast ... ]
            非 0 元素          全部是 0           还没扫描
        '''
        for fast in range(len(nums)):
            #the element want to preserve and put front
            if nums[fast]!=0:
                nums[slow],nums[fast] = nums[fast],nums[slow]
                slow += 1
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