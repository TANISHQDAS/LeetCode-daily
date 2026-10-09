class Solution:
    def minInsertions(self, s: str) -> int:
        a=b=c=0
        for x in s:
            if x=='(':
                if a%2:
                    c+=1
                    a-=1
                a+=2
            else:
                a-=1
                if a<0:
                    b+=1
                    a+=2
        return a+b+c