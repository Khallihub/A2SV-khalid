class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokens = defaultdict(int)
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime
        # print("generate", self.tokens)

    def renew(self, tokenId: str, currentTime: int) -> None:
        # print("renew",self.tokens)
        # print(self.tokens[tokenId],self.timeToLive)
        if tokenId in self.tokens and self.tokens[tokenId] + self.timeToLive > currentTime:
            self.tokens[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        # print(self.tokens)
        cnt = 0
        for k,v in self.tokens.items():
            # print(v, self.timeToLive, currentTime, v + self.timeToLive > currentTime)
            if v + self.timeToLive > currentTime:
                # print(v)
                cnt += 1
        return cnt
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)