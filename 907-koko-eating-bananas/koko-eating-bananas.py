class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        #k取value：0-len(n)
        #pile<=k:吃掉当前pile不多吃
        #pile>k:只吃里面的k个 剩下的留着接下来吃
        #virtual: kl = [i for i in range(1,max(piles)+1)
        kmin = max(piles)
        if len(piles)==h:
            return kmin
        low,high = 1, kmin
        def finish(k):
            rt = h
            for i in piles:
                t = (i+k-1)//k
                if t>rt:
                    return False
                else:
                    rt -= t
            return True
        while low<high:
            m = (low+high)//2
            if finish(m):
                high = m
            else:
                low = m+1
        return low
        

'''分析binarysearch怎么做
这里 每个pile根据新k算时间 肯定是少不了
但是可以减少k的查询次数 -> binarysearch
先看k=mid
'''

