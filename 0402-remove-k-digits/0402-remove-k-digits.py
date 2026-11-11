class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        n=len(num)
        st=[]
        if k==n:
            return '0'
        for i in range(0,n):
            while(st and k>0 and (st[-1]>num[i])):
                st.pop()
                k-=1
            if (st):
                st.append(num[i])
            else:
                if (num[i]!='0'):
                    st.append(num[i])
        while k!=0 and st:
            st.pop()
            k-=1
        return "".join(st) if st else "0"