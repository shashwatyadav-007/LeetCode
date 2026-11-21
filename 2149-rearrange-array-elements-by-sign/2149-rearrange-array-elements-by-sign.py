class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 0
        n = 1
        result = [0]*len(nums)
        for i in nums:
            if i>0:
                result[p]=i
                p+=2
            else:
                result[n]= i
                n +=2
        return result
