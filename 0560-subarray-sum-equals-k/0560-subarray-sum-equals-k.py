class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        prefixsum={0:1}
        currsum=0
        for i in nums:
            currsum=currsum+i
            diff=currsum-k
            count = count + prefixsum.get(diff,0)

            prefixsum[currsum]=1+prefixsum.get(currsum,0)
        return count


