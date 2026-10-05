class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #method 1: str method use in to check
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()','')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return True if s=='' else False
        