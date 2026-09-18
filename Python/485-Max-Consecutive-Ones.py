class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxs=1
        count=1
        for i in range(0,len(nums)):
            if nums[i]==1:
                count+=1
            else:
                count=0    
            if maxs<count:
                maxs=count
        return maxs            
        