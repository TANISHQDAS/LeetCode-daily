class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        a=b=c=d=0
        x=t
        while x%2==0: x//=2;a+=1
        while x%3==0: x//=3;b+=1
        while x%5==0: x//=5;c+=1
        while x%7==0: x//=7;d+=1
        if x!=1: return "-1"
        dp=[[0]*(b+1) for _ in range(a+1)]
        opt=((1,0),(0,1),(2,0),(1,1),(3,0),(0,2))
        for i in range(a+1):
            for j in range(b+1):
                if i==0 and j==0: continue
                bv=10**9
                for dx,dy in opt:
                    pi=i-dx if i>dx else 0
                    pj=j-dy if j>dy else 0
                    if pi==i and pj==j: continue
                    v=dp[pi][pj]+1
                    if v<bv: bv=v
                dp[i][j]=bv
        def dg(v):
            if v==2:return(1,0,0,0)
            if v==3:return(0,1,0,0)
            if v==4:return(2,0,0,0)
            if v==5:return(0,0,1,0)
            if v==6:return(1,1,0,0)
            if v==7:return(0,0,0,1)
            if v==8:return(3,0,0,0)
            if v==9:return(0,2,0,0)
            return(0,0,0,0)
        def bld(L,ra,rb,rc,rd):
            if dp[ra][rb]+rc+rd>L: return None
            r=[]
            for k in range(L):
                for g in range(1,10):
                    e2,e3,e5,e7=dg(g)
                    na=ra-e2 if ra>e2 else 0
                    nb=rb-e3 if rb>e3 else 0
                    nc=rc-e5 if rc>e5 else 0
                    nd=rd-e7 if rd>e7 else 0
                    if dp[na][nb]+nc+nd<=L-k-1:
                        ra,rb,rc,rd=na,nb,nc,nd
                        r.append(str(g))
                        break
            return ''.join(r)
        n=len(num)
        p2=[0]*(n+1);p3=[0]*(n+1);p5=[0]*(n+1);p7=[0]*(n+1)
        fz=n
        for i,ch in enumerate(num):
            v=int(ch)
            if v==0 and fz==n: fz=i
            e2,e3,e5,e7=dg(v)
            p2[i+1]=p2[i]+e2;p3[i+1]=p3[i]+e3;p5[i+1]=p5[i]+e5;p7[i+1]=p7[i]+e7
        if fz==n and p2[n]>=a and p3[n]>=b and p5[n]>=c and p7[n]>=d:
            return num
        hi=fz if fz<n-1 else n-1
        for i in range(hi,-1,-1):
            od=int(num[i])
            for g in range(od+1,10):
                e2,e3,e5,e7=dg(g)
                ra=a-p2[i]-e2; ra=ra if ra>0 else 0
                rb=b-p3[i]-e3; rb=rb if rb>0 else 0
                rc=c-p5[i]-e5; rc=rc if rc>0 else 0
                rd=d-p7[i]-e7; rd=rd if rd>0 else 0
                rl=n-1-i
                if dp[ra][rb]+rc+rd<=rl:
                    sfx=bld(rl,ra,rb,rc,rd)
                    return num[:i]+str(g)+sfx
        L0=dp[a][b]+c+d
        L=n+1 if n+1>L0 else L0
        return bld(L,a,b,c,d)