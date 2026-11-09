class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        matching_bracket={')':'(','}':'{',']':'['}
        for char in s:
            if char in matching_bracket:
                top_element=stack.pop() if stack else '#'
                if matching_bracket[char]!=top_element:
                    return False
            else:
                stack.append(char)
        
        return not stack
