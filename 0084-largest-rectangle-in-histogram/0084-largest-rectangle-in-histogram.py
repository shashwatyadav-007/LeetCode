class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack=[]
        maxi=0
        n=len(heights)
        for i in range(n):
            while(stack and heights[stack[-1]]>heights[i]):
                ele=stack[-1]
                stack.pop()
                nse=i
                if not stack:
                    pse=-1
                else:
                    pse=stack[-1]
                maxi=max(maxi,heights[ele]*(nse-pse-1))
            stack.append(i)
        while stack:
            nse=n
            ele=stack[-1]
            stack.pop()
            if stack:
                pse=stack[-1]
            else:
                pse=-1
            maxi=max(maxi,heights[ele]*(nse-pse-1))
        return maxi
