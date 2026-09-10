class Solution(object):
    def searchRange(self, nums, target):
        def search(left_side):
            left,right=0,len(nums)-1
            i=-1
            while left<=right:
                m=(left+right)//2
                if nums[m]>target:
                    right=m-1
                elif nums[m]<target:
                    left=m+1
                else:
                    i=m
                    if left_side:
                        right=m-1
                    else:
                        left=m+1 
            return i
        return [search(True),search(False)] 


