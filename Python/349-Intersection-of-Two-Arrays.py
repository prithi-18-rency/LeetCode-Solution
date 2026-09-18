class Solution(object):
    def intersection(self, nums1, nums2):
        res=[]
        for i in nums2:
            if i in nums1:
                res.append(i)
        s=set(res)
        return list(s)        
