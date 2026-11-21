class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi=float('-inf')
        summ=0
        for i in range(len(nums)):
            summ+=nums[i]
            maxi=max(maxi,summ)
            if summ<0:
                summ=0
        return maxi