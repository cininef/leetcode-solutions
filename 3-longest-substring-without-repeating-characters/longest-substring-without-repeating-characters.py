class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window：idea与快慢指针类似；但现在关注的是整个slow,fast之间这个窗口 都是candidate答案
        #快慢指针 ： 保留 [0,slow)
        #slidingwindow slow,fast = [l,r]
        #跟快慢指针类似  l 才是我们最后保留的最新valid
        l = 0
        #extra: 需要一个set记录每一次的[l,r]，直到返回题目要求
        state = set()
        res = 0
        for r in range (len(s)):
            #这里 要先清r在state set里面重复的元素和重复元素左边的所有
            while s[r] in state:
                state.remove(s[l])
                l += 1
            state.add(s[r])
            res = max(res,len(state))
        return res
'''
l = 0
state = ...                    # 窗口状态：set / 计数 dict / 和
for r in range(len(s)):        # r 每轮往右扩一步
    把 s[r] 加入 state   #一定把r先加入set里面
    #每一轮 while 结束后，[l, r] 就是以 r 结尾的、最长的、没有重复的子串
    while 窗口不合法:           # 不合法 → l 往右缩，直到重新合法
        把 s[l] 移出 state
        l += 1
    ans = max(ans, r - l + 1)  # 此时 [l, r] 合法，更新答案
'''
