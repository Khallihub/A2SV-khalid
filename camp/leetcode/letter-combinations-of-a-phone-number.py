class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        mapping =  {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        def backtrack(cur, index):
            if len(cur) == len(digits):
                if len(cur) > 0:
                    result.append("".join(cur))
                return
            
            for i in range(len(mapping[digits[index]])):
                cur.append(mapping[digits[index]][i])
                backtrack(cur,index+1)
                cur.pop()

        backtrack([],0)
        return result