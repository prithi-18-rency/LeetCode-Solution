class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums3=nums1+nums2
        nums3=sorted(nums3)
        n=len(nums3)
        if n%2==1:
            return nums3[n//2]
        else:
            return (nums3[n//2-1]+nums3[n//2])/2.0   
          

       
        