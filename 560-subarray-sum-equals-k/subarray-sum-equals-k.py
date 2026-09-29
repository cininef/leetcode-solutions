class Solution(object):
    def subarraySum(self, nums, k):
        d = dict()
        result = 0
        d[0] = 1
        
        for idx, i in enumerate(nums):
            # 1. 不要 csum 了！直接把前一个位置的雪球加到当前的 i 身上
            if idx >= 1:
                i += nums[idx - 1]
                nums[idx] = i   # 把滚大后的雪球存回原数组，供下一步用
                
            # 2. 现在 i 是从头滚到这里的总和，砍掉前面多余的 (i - k)，剩下的就是 k！
            target = i - k
            
            # 下面第 22~29 行完全保留你原来的代码，一字不改！
            if target in d:
                result += d[target]
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
                
        return result