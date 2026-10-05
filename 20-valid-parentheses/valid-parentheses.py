class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #method 2: stack
        stack = []
        close_dict = {'}':'{', ']':'[',')':'('}

        for i in s:
            # if given it's a close 
            if i in close_dict:
                #if stack is not empty and stack top is open 因为open可以堆在stack无人配对 但是进来一个close必须能和之前match
                #并且 close出现的顺序和open相反 [{ }] LIFO
                if stack and stack[-1] == close_dict[i]:
                    stack.pop()
                    continue
                else:
                    return False
            else:
                stack.append(i)
        return stack == []
        