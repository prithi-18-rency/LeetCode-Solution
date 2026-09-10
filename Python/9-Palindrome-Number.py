class Solution(object):
    def isPalindrome(self, x):
        x=str(x)
        x=x.lower().replace(" ","")
        if x==x[::-1]:
            return True
        else:
            return False    
        