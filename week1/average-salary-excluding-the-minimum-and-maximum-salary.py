class Solution:
    def average(self, salary: List[int]) -> float:
        total = sum(salary)
        min_ = total
        max_ = 0
        for i in salary:
            if i > max_:
                max_ = i
            if i < min_:
                min_ = i
        total = total - min_ - max_
        return total / (len(salary )-2)

        