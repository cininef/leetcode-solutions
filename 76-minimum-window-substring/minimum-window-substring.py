class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def valid():
            for j in t_state:
                if state.get(j, 0) < t_state[j]:
                    return False
            return True

        l = 0
        state = {}
        t_state = {}
        start = 0                # 最短窗口的起点
        min_len = float('inf')   # 最短窗口的长度，求最短所以初始为无穷大
        for i in t:
            t_state[i] = t_state.get(i, 0) + 1

        for r in range(len(s)):
            # ① r 进来：一定加，不挑
            state[s[r]] = state.get(s[r], 0) + 1
            # ② 窗口合法时，先记答案，再移除 l，试试更短
            # 合法 = 对 t 里的每个字母，state 的次数 >= t_state 的次数
            while valid():
                # ③ 比历史最短还短才更新，只记起点和长度，不切片
                if r - l + 1 < min_len:
                    start = l
                    min_len = r - l + 1
                state[s[l]] -= 1
                l += 1
            # 出了 while：窗口已经不合法，不记，等 r 继续扩

        # 最后才切一次；min_len 没变过说明没找到
        return "" if min_len == float('inf') else s[start:start + min_len]

'''
理解
1. [l,r] 要覆盖 t：s 可以有多余元素，但 t 里的每个字母都要够数
eg. state = {"a":1,"n":2,"b":1}, t_state = {"a":1,"b":1} ✅ 合法
    对 t 里的每个字母，窗口的次数 >= t 的次数
'''