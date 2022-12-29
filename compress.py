class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        right = 0
        i = 0
        while right < len(chars):
            if right < len(chars)-1 and  chars[left] == chars[right+1]:
                count = 0
                while right< len(chars) and chars[left] == chars[right]:
                    right += 1
                    count += 1
                x = 1
                for i in str(count):
                    chars[left+x] = i
                    x+=1

                left += 2
                left += len(str(count))-1
                while left < right:
                    chars[left] = 8
                    left += 1
                left = right

            else:
                left += 1
                right += 1
        print(chars)
        for i in range(len(chars)):
            if 8 in chars:
                chars.remove(8)
        return len(chars)
