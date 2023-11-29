class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(len(strs)):
            while prefix and prefix != strs[i][0:len(prefix)]:
                prefix = prefix[:-1]
        return prefix