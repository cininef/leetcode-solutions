class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        state = {}
        res = 0
        #longest repeating strategy: how to change it
        for r in range(len(s)):
            # ① r 进来：一定加，不挑
            state[s[r]] = state.get(s[r],0)+1
            # ② 2A/2C：不合法 → l 不断移除，直到合法
            #制定l移动的规则：是不合法？
            #由于max_occ是历史最大 
            #r-l+1 = window size = valid窗口长度
            #每一次检查当前最大value 是否valid
            #分析前面r可能的情况 
            #1.要不r是让maxvalue变大 -> 那么很简单 不会走while 因为r-l+1 == maxvalue+k l不变
            #2.要不就是让maxvalue不变 更新其他的出现次数 -> 这种时候必须开始更新了 从l开始 r-l+1 > maxvalue+k 缩小区间知道回归等于，同时maxvalue随着drop 已经不是当前的开始循环的maxvalue 可能被移除 换成之前第二大元素
            while r-l+1-max(state.values())>k:
                state[s[l]] -= 1
                l += 1
            #这里 维护max_occ这个str的方法有问题 当l不断移动 现在最新的max_occ也在变化
            #所以 应该变更更新方法 max_occ只要是历史最大的次数就可 完全不用去check现在state里面最大次数 他只是一个元素曾经出现的最大次数
            if res<r-l+1:
                res = r-l+1
        return res



'''
首先理解题目 分成两层；
1.知道了k 到底把换成哪个字母：肯定是window最多的 occurence最多的
2.怎么能保证在这个window occurency最多呢》肯定不是全局最多 因为如果分散但全局最多 还不如次多的
-> 其实 当前的次数 o+k如果>=window 就能保证撑满对吗 ✅
window应该是 最多occurence的元素+剩下其余所有的个数<=k就能撑满window
o+k如果 < window 需要移动到 这个max第一次occ的地方
'''