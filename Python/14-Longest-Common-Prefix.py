class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = strs[0]
        for word in strs:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
        return prefix
        