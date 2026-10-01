class Solution(object):
    def findLatestStep(self, arr, m):
        """
        :type arr: List[int]
        :type m: int
        :rtype: int
        """
        d = {}
        count_m = 0       # 记录当前屏幕上有多少个长度【恰好为 m】的区间
        latest_step = -1  # 记录最后一次 count_m > 0 的步数
        
        # 这里的 cur 就是每次要把 0 变成 1 的那个位置坐标
        for step, cur in enumerate(arr, 1):  # step 从 1 开始数
            
            # 1. 照抄 128 题：向左右邻居打听它们所在区间的长度
            left = d.get(cur - 1, 0)
            right = d.get(cur + 1, 0)
            
            # 2. 照抄 128 题：算出连在一起后的新总长
            length = left + right + 1
            
            # 3. 照抄 128 题：只更新最左端点和最右端点的长度（以及自己占位）
            d[cur - left] = length
            d[cur + right] = length
            d[cur] = length  
            
            # --------------------------------------------------
            # 下面是这道题唯一多出来的一小块“记账”逻辑：
            # 如果左边或右边原本是长度为 m 的区间，现在连上 cur 被破坏了，数量减 1
            if left == m:
                count_m -= 1
            if right == m:
                count_m -= 1
            
            # 如果新拼成的大区间长度恰好是 m，数量加 1
            if length == m:
                count_m += 1
                
            # 只要当前场上还有长度为 m 的区间，就更新最新步数
            if count_m > 0:
                latest_step = step
            # --------------------------------------------------

        return latest_step
        