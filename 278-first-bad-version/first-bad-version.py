# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        #对应10.2 duplicates找insertion point 也就是左边界
        l,h = 1, n
        while l<h:
            m = (l+h)//2
            # m already a bad version, what if more on [l,m]
            if isBadVersion(m):
                h = m
            else:
                l = m+1
        return l
        