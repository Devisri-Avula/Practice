A = [[1,3],[2,6],[8,10],[15,18]]
A.sort(key= lambda A:A[0])
n = len(A)
ans =[]
s=[]
e =[]
for i in A:
    s.append(i[0])
    e.append(i[1])
L = s[0]
R = e[0]
for i in range(1,n):
    if s[i]<R:
        R= max(R,e[i])
    else:
        ans.append([L,R])
        L= s[i]
        R =e[i]
ans.append([L,R])
print(ans)
