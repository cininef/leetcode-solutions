class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        m = 0
        for i in nums:
            #if i==1: means still consecutive, still accumulate this result, continue update m
            #else i!=1: means current 1 is broken, therefore this result is ended, check whether it can replace previous m, then reset result count
            if i == 1:
                result += 1    
                if result > m:
                    m = result
            #优化点：i=0说明result不会更新 所以不用check是否>m
            else:
                result = 0
        return m