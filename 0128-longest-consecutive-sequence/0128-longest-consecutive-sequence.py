class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset=set(nums)
        longest=0
        for num in numset:
            if num-1 not in numset:
                current=num
                count=1
                while current+1 in numset:
                    current+=1
                    count+=1
                if count>longest:
                    longest=count
                    
        return longest 