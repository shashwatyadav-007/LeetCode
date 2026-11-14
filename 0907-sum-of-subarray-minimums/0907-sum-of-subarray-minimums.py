class Solution(object):
    def findnse(self,arr):
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
    
    def findpse(self,arr):
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


    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n=len(arr)
        nse=self.findnse(arr)
        pse=self.findpse(arr)
        total=0
        mod=10**9+7
        for i in range(n):
            left=i-pse[i]
            right=nse[i]-i
            total=(total+(left*right*arr[i])%mod)%mod
        return total