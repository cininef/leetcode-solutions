class Solution:
    def maxArea(self, height: list[int]) -> int:
        # two pointer： bounded area 指针从两端往中间走
        # 无论如何两段至少width够长
        # h = min(l,r)
        # 移动短的才是bottleneck
        l,r = 0,len(height)-1
        res = 0
        while l<r:
            h = min(height[l],height[r])
            area = (r-l)*h
            if area>res:
                res = area
            if height[l]<= height[r]:
                l = l+1
            else:
                r = r-1
        return res
