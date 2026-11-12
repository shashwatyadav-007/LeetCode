class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        st=[]
        for a in asteroids:
            while st and a<0 and st[-1]>0:
                if st[-1]<abs(a):
                    st.pop()
                    continue
                elif st[-1]==abs(a):
                    st.pop()
                break
            else:
                st.append(a)
        return st