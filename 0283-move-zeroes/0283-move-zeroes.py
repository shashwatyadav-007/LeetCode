class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l=0
        n=len(nums)
        for r in range(n):
            if nums[r]:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
        return nums