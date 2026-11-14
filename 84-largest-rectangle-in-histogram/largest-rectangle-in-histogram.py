class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        #记住 一旦要调用stack[-1]一定记得确保not stack/考虑stack为空
        #跟contain water two pointer乍一看很像
        #binarysearch：判断 unsorted 所以不用
        #twopointers:不是找左右区间 而是重点在中间的元素 区间min重要
        #l,r;stack共同点 就是每次新加入的元素r/stack append 都会被处理 根据这个再对之前元素进行处理
        area = 0
        stack = []
        #思考 loop over all elements是必须的 怎么loop一边就知道所有可能的area长度
        #如果想让自己=h，那么左右延伸都要是最小的 遇到比自己小的就失效了
        #存一个元素 肯定不行 就是2156这样pop append
        #stack = [index，左边长度] 弹出的时候自动知道右边的长度
        #这样stack里面存的永远是当前见到的小 然后逐个把前面更大元素弹出去
        #width = 左边最大 + 自己 + 弹出时右边大小
        #用0把最后stack所有东西顶出去
        heights.append(0)
        for i in range(len(heights)):
            h = heights[i]
            j = None
            #step 1:决定pop规则=当前元素是小 一直把前面的都pop出来 说明前面的都到自己右边极限了
            while stack and h < heights[stack[-1][0]]:
                j = stack.pop()
                #j = [index,左边长度]
                #jarea = 自己的heights*width
                jarea = heights[j[0]] * (j[1]+i-j[0])
                area = max(area,jarea)
            #step 2：如何处理当前的 append进去 stack[index,左边长度怎么写]
            #！！！重要trick 前面的while不停在更新stack所以这时候不能用原条件写if判断stack怎么append
            #j是最后一个 > h的元素
            #consider 没进while=stack一开始就是空的/h>stack顶上 就不能用j了
            if not j:
                stack.append((i,0))
            #剩下只要进来了while 有更新stack的 用j
            else:
                stack.append((i,j[1]+i-j[0]))
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

