class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        st1=[]
        st2=[]
        for ch in s:
            if ch=='#':
                if st1:
                    st1.pop()
            else:
                st1.append(ch)
    
        for ch in t:
            if ch=='#':
                if st2:
                    st2.pop()
            else:
                st2.append(ch)
        return st1==st2
             