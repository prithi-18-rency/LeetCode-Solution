class Solution(object):
    def singleNumber(self, nums):
        count=set()
        for i in nums:
           if i in count:
            count.remove(i)
           else:
            count.add(i)
        return count.pop()     
              