import numpy as np
m,n=map(int,input().split())
x=np.zeros(m)
for i in range(n):
    a,b,c=map(int,input().split())
    for i in range(a-1,b):
        x[i]=x[i]+c
print(int(max(x)))
