class Solution(object):
    def removeElement(self, nums, val):
        res=[]
        for i in nums:
            if i!=val:
                res.append(i)
        for i in range(len(res)):
            nums[i]=res[i]
        return len(res)        
