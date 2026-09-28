class Solution(object):
    def longestConsecutive(self, nums):
        dict = {}
        result = 0

        # 优化1：先用 set 去重 + 直接遍历元素（省掉 range 和重复判断）
        for cur in set(nums):
            
            # 分支1：左右都在 -> 合并两段区间
            if cur - 1 in dict and cur + 1 in dict:
                L = dict[cur - 1][0]
                R = dict[cur + 1][1]
                new = [L, R]
                dict[L] = new
                dict[R] = new
                # (因为开头 set 去重了，cur 以后绝不会再出现，连 dict[cur] = new 都可以省掉！)
                
            # 分支2：只有左邻居在 -> cur-1 必是右端点，直接把它的右边界改成 cur
            elif cur - 1 in dict:
                L = dict[cur - 1][0]
                R = cur
                dict[cur - 1][1] = cur
                dict[cur] = dict[cur - 1]  # reference 共享同一个 list
                
            # 分支3：只有右邻居在 -> cur+1 必是左端点，直接把它的左边界改成 cur
            elif cur + 1 in dict:
                L = cur
                R = dict[cur + 1][1]
                dict[cur + 1][0] = cur
                dict[cur] = dict[cur + 1]  # reference 共享同一个 list
                
            # 分支4：左右都不在 -> 自己成一段
            else:
                L = R = cur
                dict[cur] = [cur, cur]

            # 优化2：边建表边更新最大长度，省掉最后遍历一次 dict.values()
            if R - L + 1 > result:
                result = R - L + 1

        return result