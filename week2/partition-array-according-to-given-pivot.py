class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        piv = []
        greater = []
        for i in nums:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                piv.append(i)
            else:
                greater.append(i)
        print(less, greater)
        return [*less, *piv, *greater]