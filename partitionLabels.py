class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        location = {}
        ans = []
        for i in range (len(s)):
            location[s[i]] = i
        left = 0
        size = 0
        while left < len(s):
            # print(left)
            right = location[s[left]]
            i = left
            if right == left:
                ans.append(1)
                left += 1
                continue
            while i < right:
                if location[s[i]] > right:
                    right = location[s[i]]
                else:
                    size = right+1
                i+=1
            ans.append(size-left)       
            left = size 
        return ans
