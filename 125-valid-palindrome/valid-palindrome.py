class Solution:
    def isPalindrome(self, s: str) -> bool:
        #m2: two pointer 对撞
        l,r = 0, len(s)-1
        while l<r:
            #case1: l or r is not alphanumeric -> skip l+=1/r+=1
            #case2:l is alphanumeric and r is alphanumeric and both lowercase equal: all skip +1
            #case3:l is alphanumeric and r is alphanumeric and not equal: return false
            while l<r and not s[l].isalnum():
                l += 1
            while l<r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True 

