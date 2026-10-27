class Solution:
    def trap(self, height: list[int]) -> int:
        #理解规则 应该从每个柱子最大的储水量开始一一计算
        l,r = 0, len(height)-1
        area = 0
        lmax = rmax = 0
        while l<r:
            lmax = max(height[l],lmax)
            rmax = max(height[r],rmax)
            if lmax<rmax:
                area += lmax - height[l]
                l += 1
            else:
                area += rmax - height[r]
                r -= 1
        return area


'''
事实 1：每根柱子宽度是 1;所以总水量 = 每一列的水加起来。
问题变成：第 i 列能存几格水？

事实 2：水会往低处流:第 i 列上方的水，只要左边或右边有一条路能流出去，就会流走。
所以水能停住，必须左右两边都有墙挡着。

推论 1：左边能挡多高？
左边所有墙里，最高的那堵决定左边最多能挡多高。比它高的水会从左边漫过去。→ 左边能挡到 左边最高

推论 2：右边能挡多高？同理 → 右边能挡到 右边最高

推论 3：水面有多高？
两边都要挡住才行，所以由矮的那边决定：→ 水面 = min(左边最高, 右边最高)
分析 对于每一次 第i列 他的左右
左边最高=lmax已经走过了 右边最高>=rmax;右边只走到rmax可能还有比rmax更高的
if lmax<rmax:说明min这时候选lmax 右边绝不可能成为流水的原因 所以说应该去更新第l列 这个是明确的=知道水面 = min(左边最高, 右边最高)=左边最高
第r列的水没有这个条件

推论 4：这一列有几格水？
水面以下，有一部分被柱子自己占掉了：→ 水 = 水面 - height[i]
'''

            