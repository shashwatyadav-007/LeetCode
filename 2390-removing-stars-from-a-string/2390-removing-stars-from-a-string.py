class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        st=[]
        for ch in s:
            if ch=='*':
                st.pop()
            else:
                st.append(ch)
        return ''.join(st)