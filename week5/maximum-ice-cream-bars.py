class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        cnt = [0] * (max(costs)+1)
        for i in costs:
            cnt[i] += 1
        quantity = 0
        print(cnt)
        for i in range(1,max(costs)+1):
            print(coins,quantity)
            if coins - i*cnt[i] >= 0:
                quantity += cnt[i]
                coins -= i*cnt[i]
            else:
                print("kda", coins,quantity)
                if coins - i >= 0:
                    while coins - i >= 0:
                        coins -= i
                        quantity += 1
                else:
                    break
        return quantity