A = [1, -2, 1, 2]
n = len(A)
pf =[]
hm={}
ans =[]
pf.append(A[0])
for i in range(1,n):
    temp = pf[i-1]+A[i]
    pf.append(temp)
for i in pf:
    if i in hm:
        hm[i]+=1
    else:
        hm[i]=1
for i in hm:
    if hm[i]>1:
        arr=[]
        for j in range(n):
            if i==pf[j]:
                arr.append(j)
        res = max(arr) - min(arr)
        ans.append(res)
    if i==0:
        res = pf.index(i)+1
        ans.append(res)
if len(ans)==0:
    print(0)
else:
    print(max(ans))
            
