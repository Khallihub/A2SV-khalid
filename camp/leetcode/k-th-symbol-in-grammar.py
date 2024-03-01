class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        print(n,k)
        if n == 1:
            return 0

        if k <= 2**(n-2): return self.kthGrammar(n-1,k)
        else:
            res = self.kthGrammar(n-1,k-2**(n-2))
            if res == 0: return 1
            else: return 0