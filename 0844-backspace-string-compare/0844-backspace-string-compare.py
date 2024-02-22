class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def builder(string):
            stack = []
            for c in string:
                if c != '#':
                    stack.append(c)
                elif stack:
                    stack.pop()
            return "".join(stack)


        
        return builder(s) == builder(t)
        