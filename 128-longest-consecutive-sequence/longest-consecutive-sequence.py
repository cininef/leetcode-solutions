class Solution(object):
    def longestConsecutive(self, nums):
        d = {}
        result = 0
        for cur in nums:                 # 直接遍历元素，省掉 range(len(nums))
            if cur in d:
                continue
            left = d.get(cur - 1, 0)     # 左邻居所在区间的长度（不在就是 0）
            right = d.get(cur + 1, 0)    # 右邻居所在区间的长度（不在就是 0）
            
            length = left + right + 1    # 新区间总长度
            d[cur] = length              # 自己占位防重
            d[cur - left] = length       # 更新最左端点 L 的长度
            d[cur + right] = length      # 更新最右端点 R 的长度
            
            if length > result:          # 顺手更新最大值，省掉最后的 dict.values() 循环
                result = length
        return result