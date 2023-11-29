
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        lst = []
        for i in range(17):
            p = pow(3, i)
            if  p <= n:
                lst.append(p)
            else:
                break
        left = len(lst) - 2
        print(lst)
        sum_ = lst[-1]
        if sum_ == n:
            return True
        while left >= 0:
            print(sum_)
            if sum_ == n:
                return True
            if sum_ + lst[left] == n:
                return True
            elif sum_ + lst[left] < n:
                sum_ += lst[left]
                left -= 1
            elif sum_ + lst[left] > n:
                left -= 1
        return False