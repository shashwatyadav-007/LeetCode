class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n=len(nums)
        left=0
        right=n-1
        first=-1
        last=-1
        while(left<=right):
            mid=(right+left)//2
            if target==nums[mid]:
                first=mid
                right=mid-1

            elif target<nums[mid]:
                right=mid-1
            else:
                left=mid+1
        left=0
        right=n-1
        while(left<=right):
            mid=(right+left)//2
            if target==nums[mid]:
                last=mid
                left=mid+1

            elif target<nums[mid]:
                right=mid-1
            else:
                left=mid+1
            
        return [first,last]
