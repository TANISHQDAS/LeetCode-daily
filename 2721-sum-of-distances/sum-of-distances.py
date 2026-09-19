class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        d={}
        r=[0]*len(nums)
        for i,x in enumerate(nums):
            c,s=d.get(x,(0,0))
            r[i]+=i*c-s
            d[x]=(c+1,s+i)
        d={}
        for i in range(len(nums)-1,-1,-1):
            x=nums[i]
            c,s=d.get(x,(0,0))
            r[i]+=s-i*c
            d[x]=(c+1,s+i)
        return r