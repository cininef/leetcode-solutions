class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        #注意 search
        def binarysearch_left(nums,target):
            #写到n 因为nums为空 h要有定义
            #left search也会找到len（nums)
            l,h = 0, len(nums)
            while l<h:
                m = (l+h)//2
                # target on [l,m] might contains more
                if target <= nums[m]:
                    h = m
                else:
                    l = m+1
            #无论找没找到 都返回就是target应该在list里面的位置
            #底下再探讨情况
            '''
            l=0:
                1.如果此时nums[l]==target 说明0处就等于target 左边起始点
                2.如果此时nums[l]!=target 说明target比nums[0]还小 要插入成第一个元素=target不存在
            l=n-1:
                1.nums[l]==target 说明n-1处就等于target 左边起始点 整个list也只有这一个元素符合target
                2.nums[l]!=target 说明target比nums[l]还小 要插入成倒数第二个元素 = target不存在
            l=n:
                1.明显属于outofrange 也就是在n-1都找不到在边界范围内>=target的起点 -> -1 not find
                2.nums[l]都没有定义 无论是否相等都不行
            '''
            return l
        
        # left -> left boundary of target, need to check if not find
        # right -> left boudary of target + 1，可能找不到超出lastindex
        left = binarysearch_left(nums,target)
        right = binarysearch_left(nums,target+1)
        right_end = right - 1
        #首先探讨l l是决定了target是否存在
        #never have this element
        if left==len(nums):
            return [-1,-1]
        if nums[left]!=target:
            return [-1,-1]
        #otherwise, this element exist
        else:
            return [left,right_end]