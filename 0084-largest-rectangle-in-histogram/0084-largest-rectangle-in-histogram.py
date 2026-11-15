class Solution(object):
    def nextSmallerElement(self,arr):
        stack=[]
        n=len(arr)
        nse=[0]*n
        for i in range(n-1,-1,-1):
            while(stack and arr[stack[-1]]>=arr[i]):
                stack.pop()
            if not stack:
                nse[i]=n
            else:
                nse[i]=stack[-1]
            stack.append(i)
        return nse

    def prevSmallerElement(self,arr):
        stack=[]
        n=len(arr)
        pse=[0]*n
        for i in range(n):
            while(stack and arr[stack[-1]]>arr[i]):
                stack.pop()
            if not stack:
                pse[i]=-1
            else:
                pse[i]=stack[-1]
            stack.append(i)
        return pse

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n=len(heights)
        nse=self.nextSmallerElement(heights)
        pse=self.prevSmallerElement(heights)
        maxi=0
        for i in range(n):
            maxi=max(maxi,heights[i]*(nse[i]-pse[i]-1))
        return maxi