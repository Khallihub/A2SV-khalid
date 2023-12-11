class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        t5 = len(arr)/4
        left = None
        leftCnt = 0
        right = None
        rightCnt = 0
        print(arr)
        for i in range(len(arr)):
            print(left,right)
            if right != None and arr[i] != right:
                left = right
                leftCnt = rightCnt
                rightCnt = 1
                right = arr[i]
            else:
                right = arr[i]
                rightCnt +=1
            if rightCnt > t5:
                break
        return right
        