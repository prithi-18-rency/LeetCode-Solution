class Solution(object):
    def majorityElement(self, nums):
        res={}
        for i in nums:
            if i in res:
                res[i]+=1
            else:
                res[i]=1
        return max(res,key=res.get)            