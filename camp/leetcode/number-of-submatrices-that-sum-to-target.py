class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        sub_sum = [[0] * COLS for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                t_r = sub_sum[r-1][c] if r > 0 else 0
                t_l = sub_sum[r-1][c-1] if min(r,c) > 0 else 0
                b_l = sub_sum[r][c-1] if c > 0 else 0
                sub_sum[r][c] = matrix[r][c] + t_r + b_l - t_l
        res = 0                
        for r1 in range(ROWS):
            for r2 in range(r1, ROWS):
                diffs = defaultdict(int)
                diffs[0] = 1
                for c in range(COLS):
                    t_r = sub_sum[r1-1][c] if r1 > 0 else 0
                    cur_sum = sub_sum[r2][c] - t_r
                    diff = cur_sum - target
                    res += diffs[diff]
                    diffs[cur_sum] += 1
        return res
                    