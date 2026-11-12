class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack=[]
        n=len(nums2)
        ans=[-1]*n
        for i in range(n-1,-1,-1):
            while stack and stack[-1]<=nums2[i]:
                stack.pop()
            if stack:
                ans[i]=stack[-1]
            stack.append(nums2[i])
        result=[]
        for num in nums1:
            result.append(ans[nums2.index(num)])
        return result