class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        #记住 一旦要调用stack[-1]一定记得确保not stack/考虑stack为空
        #跟contain water two pointer乍一看很像
        #判断 unsorted：不用binarysearch
        area = 0
        stack = []
        #思考 loop over all elements是必须的 怎么loop一边就知道所有可能的area长度
        #如果想让自己=h，那么左右延伸都要是最小的 遇到比自己小的就失效了
        #存一个元素 肯定不行 就是2156这样pop append
        #stack = [index，左边长度]
        #这样stack里面存的永远是当前见到的最小 因为但凡比这个大的 遇到这个小的都被弹出去了
        for i in range(len(heights)):
            h = heights[i]
            w = 1                                              # ➕ 加：默认左边宽度只有自己
            while stack and h<heights[stack[-1][0]]:
                j = stack.pop()
                jarea = heights[j[0]] * (j[1]+i-j[0]-1)        # ✏️ 改：heights[j][0] → heights[j[0]]；i-j → i-j[0]-1
                area = max(area,jarea)
                w = i-j[0]+j[1]                                # ➕ 加：我能往左盖过 j，接上 j 的左边宽度
            stack.append((i,w))                                # ✏️ 改：i-j[0]+1 → w
        for j in stack:                                        # ➕ 加：剩下的柱子能扩到最右边
            area = max(area, heights[j[0]] * (j[1]+len(heights)-j[0]-1))
        return area


'''从brute force能看出来 如果我采取 一边不动 那么就是永远知道我现在区间长度+这段里面min 就可以得到area
这里 思考一种方式能最高效的枚举完所有结果 把heights[i]每一次作为这个rectangle的height 左右扩展直到无法扩展 = 按照len(heights)枚举完所有结果了
#理解规则 area = min(l,r)*(r-l+1)
#m1 brute force: try all the combination of l,r
area = 0
for l in range(len(heights)):
    m = heights[l]
    for r in range(l,len(heights)):
        m = min(m,heights[r])
        area = max(area,m * (r-l+1))
return area
'''

