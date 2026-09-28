class Solution:
    def maxDepth(self, s: str) -> int:
        a=0
        b=0
        for c in s:
            if c=='(':
                b+=1
                a=max(a,b)
            elif c==')' :
                b-=1
        return a            
        