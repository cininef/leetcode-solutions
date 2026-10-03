class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        seen = dict()
        #check dubplicates/这个O(1)是必备 减少后面的查找
        if len(s) != len(t):
            return False
        for s1 in s:
            if s1 in seen:
                seen[s1] += 1
            else:
                seen[s1] = 1
        for t1 in t:
            if t1 in seen:
                seen[t1] -= 1
            else:
                return False
        #all() function check every elements in "and" 
        return all(val == 0 for val in seen.values())