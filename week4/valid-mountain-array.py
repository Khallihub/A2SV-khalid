class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        tmp = False
        increasing = True
        decreasing = False
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                tmp = True
            if arr[i] > arr[i+1] and increasing:
                increasing = False
                decreasing = True
            if arr[i] == arr[i+1]:
                return False
            if arr[i] < arr[i+1] and decreasing:
                return False
        
        if tmp and decreasing:
            return True
        return False
