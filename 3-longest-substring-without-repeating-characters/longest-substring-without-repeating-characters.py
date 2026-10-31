class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window：idea与快慢指针类似；但现在关注的是整个slow,fast之间这个窗口 都是candidate答案
        #快慢指针 ： 保留 [0,slow)
        #slidingwindow slow,fast = [l,r]
        #跟快慢指针类似  l 才是我们最后保留的最新valid开始点 r负责loopover
        l = 0
        #extra: 需要一个set记录每一次的[l,r]，{"a","c","b"}正好是s里面遇到的顺序 用来得到长度
        state = {}
        res = 0
        for r in range(len(s)):
            #① r 进来：更新 state（一定加，不挑）第一件事情 永远把r加入现在最新的state里
            state[s[r]] = state.get(s[r],0)+1
            #② 判断 [l, r] 合不合法 → 不合法 决定 l 怎么动 让他合法（if 或 while，同时还回 state）
            #这里不合法是有duplicate
            while state[s[r]]>1:
                state[s[l]] -= 1
                l += 1
            #len(state) == r-l+1
            #③ 现在窗口合法了 → 更新答案
            res = max(res,r-l+1)
        return res
'''
for r in range(len(s)):
    ① r 进来：更新 state（一定加，不挑）
    ② 判断 [l, r] 合不合法 → 决定 l 怎么动（if 或 while，同时还回 state）
    ③ 现在窗口合法了 → 更新答案

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
