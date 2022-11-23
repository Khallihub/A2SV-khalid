class Solution: 
    def select(self, arr, i):
        ar = arr[i:]
        min = ar[0]
        for j in ar:
            if (j <= min):
                min = j
        return ar.index(min)
    
    def selectionSort(self, arr,n):
        j = 0
        while j < n:
            a = self.select(arr,j)+j
            temp = arr[j]
            arr[j] = arr[a]
            arr[a] = temp
            j+=1
        return arr
