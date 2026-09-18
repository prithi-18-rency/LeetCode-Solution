class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxs=0
        count=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                count=0    
            if maxs<count:
                maxs=count
        return maxs            
        