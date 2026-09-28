class Solution(object):
    def longestConsecutive(self, nums):
        dict = {}
        result = 0

        for cur in set(nums):
            # 1. 算 L：左邻居在就拿左邻居的 L，不在就是 cur 自己
            L = dict[cur - 1][0] if (cur - 1 in dict) else cur
            # 2. 算 R：右邻居在就拿右邻居的 R，不在就是 cur 自己
            R = dict[cur + 1][1] if (cur + 1 in dict) else cur
            
            # 3. 把新区间同步给最左端点 L 和最右端点 R
            new = [L, R]
            dict[L] = new
            dict[R] = new
            
            # 4. 顺手更新最大长度
            if R - L + 1 > result:
                result = R - L + 1

        return result