class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxs=count=0
        for i in range(len(nums)):
            count=count+1 if nums[i]==1 else 0
            maxs=max(count,maxs)
        return maxs    