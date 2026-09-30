class Solution:
    def convertToTitle(self, n: int) -> str:
        a = ''
        while(n>26):
            if n%26:
                a = chr((n%26)+64)+a
                n = n//26
            else:
                a = 'Z'+a
                n = (n//26)-1
        a = chr(n+64)+a
        return a