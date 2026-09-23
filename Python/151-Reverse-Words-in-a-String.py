class Solution(object):
    def reverseWords(self, s):
        s=s.split()
        res=[]
        for i in range(len(s)-1,-1,-1):
            res.append(s[i])
        return " ".join(res)   


