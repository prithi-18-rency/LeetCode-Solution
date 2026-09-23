class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        res={}
        for i in range(len(nums)):
            if nums[i] in res:
                if abs(res[nums[i]]-i)<=k:
                    return True
            res[nums[i]]=i  
        
        return False          

        