def findpos(n):
    pos =0
    while n!=0:
        pos+=1
        n = n//2
    return pos
A = 5
pos = findpos(A)
print(pos)
x = pow(2,pos-1)
ans = 1+ (2*(A-x))
print(ans)
