wt=[10,20,30]
pt=[60,100,120]
com=list(zip(wt,pt))
com.sort()
wt,pf=zip(*com)
weight=50
n=len(pf)
m=[[0 for _ in range(weight+1)] for _ in range(n+1)]
print(m)
print("pf",pf)
print("wt",wt)
for i in range(n+1):
    for j in range(weight+1):
        if i==0 or j==0 or wt[i-1]>j:
            m[i][j]=m[i-1][j]
        else:
            m[i][j]=max(pf[i-1]+m[i-1][j-wt[i-1]],m[i-1][j])
print(m)
l=[]
max_profit=m[-1][-1]
print("max",max_profit)
i=len(m)-1
while max_profit>0:
    if m[i][-1]-max_profit !=0:
        l.append(wt[i])
        max_profit-=pf[i]
    i-=1
print(max_profit)
print(l)