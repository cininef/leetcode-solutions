class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        #bs特征：sorted 一定要是sorted/规律fftt排布
        #这里 完全按照顺序排放 头尾相接
        #还是search是否存在+可能有duplicate
        m = len(matrix) # no. of rows
        n = len(matrix[0]) # no. of cols
        def flatten(k):
            row = k//n
            col = k%n
            return matrix[row][col]
        def binarysearch_left(target):
            l,h = 0,m*n
            while l<h:
                mid = (l+h)//2
                # target stays in [l,m]
                if target<=flatten(mid):
                    h = mid
                else:
                    l = mid+1
            return l
        left = binarysearch_left(target)
        if left == m*n:
            return False
        if flatten(left)!=target:
            return False
        else:
            return True
