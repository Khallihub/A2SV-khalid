class Solution:
    def minimumSteps(self, s: str) -> int:
        n=len(s)
        s1=list(s)
        i=0
        j=n-1
        cnt=0
        while i<j:
            if s1[i]=="1" and s1[j]=="0":
                s1[i],s1[j]=s1[j],s1[i]
                
                cnt+=(j-i)
                i+=1
                j-=1
            elif s1[i]=="1" and s1[j]=="1":
                j-=1
            elif s1[i]=="0" and s1[j]=="0":
                i+=1
            else:
                i+=1
                j-=1
        return cnt

            

                