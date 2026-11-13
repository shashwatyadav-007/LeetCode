class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N=len(nums)
        nqe=[-1]*N
        stack=[]
        for i in range(2*N-1,-1,-1):
            while(stack and stack[-1]<=nums[i%N]):
                stack.pop()
            if(i<N):
                if stack:
                    nqe[i]=stack[-1]
            stack.append(nums[i%N])
        return nqe